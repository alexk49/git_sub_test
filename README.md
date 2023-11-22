# Made to test sub module features

You initially add a sub module with:
```
git submodule add git-project-url
```

To update first time when running submodules pull requests run:

git submodule update --init --remote --recursive

Then further updates can be handled via 

git submodule update --recursive

Check status with:

git submodule status
