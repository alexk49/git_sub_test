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

To avoid issues with the repo, it is easiest to make changes directly to the actual project via a clone rather than making changes to git submodule and pushing from that project. This is because you might have a detached HEAD branch which is not up to date. You can stop this by changing dir to the submodule and running:

git checkout main

git pull

This will update to the latest version. And make your git tree work from the submodule project. But there seems to be potential for issues with this so it is safest to not update from the submodule.
