# mutwo-documentation

This is the code for the mutwo documentation.

## Update documentation

```bash
git checkout main
cd documentation
niv update mutwo-nix
nix-shell
./make
git checkout gh-pages
git push -f origin gh-pages
```

