# GitHub Actions Workflows

This directory contains optimized CI/CD workflows for automated testing and code quality checks.

## Workflows

### 1. Playwright Tests (`playwright-tests.yml`) ⚡
**Trigger**: Push to main/develop, Pull Requests, Manual dispatch

**Optimizations**:
- ✅ **Browser caching** - Browsers cached between runs (90% faster on cache hit)
- ✅ **Smart matrix** - All browsers on PRs, Chromium only on main/develop (saves time & cost)
- ✅ **Parallel execution** - Uses pytest-xdist to run tests in parallel
- ✅ **Pip caching** - Python dependencies cached automatically
- ✅ **25-minute timeout** - Prevents hanging jobs

**What it does**:
- **On PRs**: Runs full test suite across all three browsers (Chromium, Firefox, WebKit)
- **On main/develop**: Runs quick Chromium tests only
- Generates HTML reports for each browser
- Uploads test reports and screenshots as artifacts
- Installs only the specific browser needed per matrix job

**Artifacts**:
- `test-report-{browser}` - HTML reports in `reports/` directory (kept 30 days)
- `screenshots-{browser}` - Failure screenshots (kept 30 days)

### 2. Docker Build Validation (`docker-tests.yml`) 🐳
**Trigger**: PRs to main/develop, Push to main, Tags, Manual dispatch

**Optimizations**:
- ✅ **Only Chromium** - Installs only Chromium browser (75% smaller image)
- ✅ **Runs only when needed** - PRs and main branch, not on feature pushes
- ✅ **Docker Buildx** - Faster builds with caching support
- ✅ **Correct volume mounts** - Uses directory mounts for reports, not file mounts

**What it does**:
- Validates Docker build succeeds
- Runs full test suite in containerized environment
- Ensures production Docker image works correctly
- Tests with pytest-ci.ini configuration

**Use case**: Validates Docker deployment before merges and releases

**Artifacts**:
- `docker-test-report` - HTML report from `reports/` directory (kept 30 days)
- `docker-screenshots` - Failure screenshots (kept 30 days)

### 3. Code Quality (`lint.yml`) 🔍
**Trigger**: PRs to main/develop, Push to main/develop

**Optimizations**:
- ✅ **Only on PRs/main** - No longer runs on every feature push
- ✅ **Lightweight** - No browser installation needed

**What it does**:
- Checks code formatting with Black
- Checks import sorting with isort
- Lints code with Flake8
- Enforces basic Python code quality standards

**Note**: Formatting checks are non-blocking (continue-on-error) but provide warnings

## Viewing Results

### In GitHub UI:
1. Go to **Actions** tab in your repository
2. Click on a workflow run to see results
3. Download artifacts from the **Artifacts** section at the bottom

### Status Badges:
Add these to your README.md to show build status:

```markdown
![Playwright Tests](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/playwright-tests.yml/badge.svg)
![Docker Tests](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/docker-tests.yml/badge.svg)
![Code Quality](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/lint.yml/badge.svg)
```

## Manual Workflow Dispatch

Both test workflows support manual triggering:
1. Go to **Actions** tab
2. Select the workflow
3. Click **Run workflow**
4. Choose the branch and click **Run workflow**

## Configuration

### Matrix Testing
The Playwright workflow uses matrix strategy to test across browsers:
- Chromium
- Firefox  
- WebKit

### Caching
- Python dependencies are cached using `cache: 'pip'`
- Docker layers are cached with Buildx

## Customization

### Run specific tests:
Edit the test command in the workflow file:
```yaml
run: pytest tests/test_text_box.py --browser=${{ matrix.browser }}
```

### Change Python version:
Update the `python-version` in setup-python step:
```yaml
python-version: '3.12'
```

### Adjust artifact retention:
Change `retention-days` value (default: 30 days)
