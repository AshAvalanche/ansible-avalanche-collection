# Developer Documentation

## Change Log Generation

The `CHANGELOG.md` file is generated using the [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator) Docker image. To update the `CHANGELOG.md` file, run the following command:

```bash
docker run -it --rm -v "$(pwd):/usr/local/src/your-app" githubchangeloggenerator/github-changelog-generator -u AshAvalanche -p ansible-avalanche-collection --token $GH_TOKEN
```
