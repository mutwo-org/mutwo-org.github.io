{ sources ? import ./nix/sources.nix, rsources ? import (sources.mutwo-nix.outPath + "/nix/sources.nix"), pkgs ? import rsources.nixpkgs {}}:

let

  sphinx-autodoc-annotation-origin = sources.sphinx-autodoc-annotation;
  sphinx-autodoc-annotation = pkgs.python310Packages.buildPythonPackage rec {
    name = "sphinx-autodoc-annotation";
    src = pkgs.fetchFromGitHub {
      owner = sphinx-autodoc-annotation-origin.owner;
      repo = sphinx-autodoc-annotation-origin.repo;
      rev = sphinx-autodoc-annotation-origin.rev;
      sha256 = sphinx-autodoc-annotation-origin.sha256;
    };
    propagatedBuildInputs = [
        pkgs.python310Packages.sphinx
    ];
    doCheck = false;
  };

  autodocsumm-origin = sources.autodocsumm;
  autodocsumm = pkgs.python310Packages.buildPythonPackage rec {
    name = "autodocsumm";
    src = pkgs.fetchFromGitHub {
      owner = autodocsumm-origin.owner;
      repo = autodocsumm-origin.repo;
      rev = autodocsumm-origin.rev;
      sha256 = autodocsumm-origin.sha256;
    };
    propagatedBuildInputs = [
        pkgs.python310Packages.sphinx
        pkgs.python310Packages.versioneer
    ];
    doCheck = false;
    preBuild = ''
cat > setup.py << EOF
from setuptools import setup

install_requires = [
  'sphinx>=3.0',
]

setup(
  name='autodocsumm',
  description='autodocsumm description',
  version='v0.2.11',
  install_requires=install_requires,
)
EOF
  '';
  };


  autoclasstoc-origin = sources.autoclasstoc;
  autoclasstoc = pkgs.python310Packages.buildPythonPackage rec {
    name = "autoclasstoc";
    src = pkgs.fetchFromGitHub {
      owner = autoclasstoc-origin.owner;
      repo = autoclasstoc-origin.repo;
      rev = autoclasstoc-origin.rev;
      sha256 = autoclasstoc-origin.sha256;
    };
    propagatedBuildInputs = [
        # see https://github.com/kalekundert/autoclasstoc/blob/881da02/pyproject.toml#L17-L19
        pkgs.python310Packages.sphinx
        pkgs.python310Packages.docutils
        pkgs.python310Packages.more-itertools
    ];
    doCheck = false;
    preBuild = ''
cat > setup.py << EOF
from setuptools import setup

install_requires = [
  'sphinx>=3.0',
  'docutils',
  'more_itertools',
]

setup(
  name='autoclasstoc',
  description = "autoclasstoc",
  version='1.6.0',
  install_requires=install_requires,
)
EOF
  '';

  };

  mutwo-core      = import (sources.mutwo-nix.outPath + "/mutwo.core/default.nix") {};
  mutwo-timeline  = import (sources.mutwo-nix.outPath + "/mutwo.timeline/default.nix") {};
  mutwo-common    = import (sources.mutwo-nix.outPath + "/mutwo.common/default.nix") {};
  mutwo-music     = import (sources.mutwo-nix.outPath + "/mutwo.music/default.nix") {};
  mutwo-midi      = import (sources.mutwo-nix.outPath + "/mutwo.midi/default.nix") {};
  mutwo-csound    = import (sources.mutwo-nix.outPath + "/mutwo.csound/default.nix") {};
  mutwo-ekmelily  = import (sources.mutwo-nix.outPath + "/mutwo.ekmelily/default.nix") {};
  mutwo-abjad     = import (sources.mutwo-nix.outPath + "/mutwo.abjad/default.nix") {};

  mypython = pkgs.python310.buildEnv.override {
    extraLibs = with pkgs.python310Packages; [
      # mutwo modules
      mutwo-core
      mutwo-timeline
      mutwo-common
      mutwo-music
      mutwo-midi
      mutwo-ekmelily
      mutwo-csound
      mutwo-abjad

      # mutwo module extra dependencies
      pillow
      ortools

      # Auto doc building
      sphinx
      sphinx-autodoc-annotation
      autodocsumm
      autoclasstoc
    ];
  };

in

  pkgs.mkShell {
    buildInputs = with pkgs; [
          mypython
          lilypond-with-fonts
      ];
  }
