# WorkflowPro Automation Framework

A comprehensive QA automation framework for testing the WorkflowPro application using Playwright and Pytest.

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [Features](#features)
- [Contributing](#contributing)
- [Support](#support)

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+** - [Download](https://www.python.org/downloads/)
- **Git** - [Download](https://git-scm.com/downloads)
- **Node.js** (Optional) - Only needed for some Playwright tools - [Download](https://nodejs.org/)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yashkancharwale/workflowpro-automation.git
cd workflowpro-automation
```

### 2. Create and Activate Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers

```bash
python -m playwright install
```

## Configuration

### 1. Environment Configuration (`config/env.yaml`)

Set your environment base URL and browser preferences:

```yaml
environment: staging
base_url: https://staging.workflowpro.com
browser: chromium
headless: false
timeout: 30000
```

### 2. Credentials (`config/credentials.yaml`)

Add test user credentials:

```yaml
test_users:
  admin:
    email: admin@workflowpro.com
    password: your_password
    role: admin
```

**⚠️ WARNING:** Never commit actual credentials to git. Use environment variables in production.

### 3. Tenants Configuration (`config/tenants.yaml`)

Add tenant domain mappings:

```yaml
tenants:
  default:
    domain: company1.workflowpro.com
    name: Company One
    region: US
```

## Running Tests

### Run All Tests

```bash
pytest
```

### Run Specific Test File

```bash
pytest tests/test_login.py
```

### Run Tests by Marker

```bash
pytest -m smoke
pytest -m regression
```

### Run Tests with HTML Report

```bash
pytest --html=report.html --self-contained-html
```

### Run Tests in Headless Mode

```bash
# Modify env.yaml or use the command line
pytest --headless
```

### Run Tests in Parallel (requires xdist)

```bash
pytest -n auto
```

### Run Tests with Verbose Output

```bash
pytest -v
pytest -vv
```

### Run Tests and Stop on First Failure

```bash
pytest -x
```

## Project Structure

```
workflowpro-automation/
├── config/                      # Configuration files
│   ├── env.yaml                # Environment configuration
│   ├── credentials.yaml        # Test user credentials
│   └── tenants.yaml            # Tenant configuration
├── pages/                       # Page Object Models
│   ├── base_page.py            # Base page class with common methods
│   ├── login_page.py           # Login page object
│   └── dashboard_page.py       # Dashboard page object
├── tests/                       # Test files
│   ├── conftest.py             # Pytest configuration and fixtures
│   ├── test_login.py           # Login tests
│   └── test_dashboard.py       # Dashboard tests
├── utils/                       # Utility modules
│   ├── config_reader.py        # Configuration reader
│   └── test_data.py            # Test data generators
├── requirements.txt            # Python dependencies
├── pytest.ini                  # Pytest configuration
├── .gitignore                  # Git ignore rules
├── .browserstack.yml           # BrowserStack configuration
└── README.md                   # This file
```

## Features

### 🎭 Page Object Model
- Organized page object classes for maintainability
- Base page class with common methods
- Easy element selectors management

### 🧪 Test Framework
- Pytest for test execution
- Fixtures for browser and page management
- Support for test markers (smoke, regression, etc.)

### 📊 Reporting
- HTML test reports
- Allure integration ready
- Screenshot on failure capability

### 🌐 Multi-Browser Support
- Chromium
- Firefox
- WebKit

### ☁️ BrowserStack Integration
- Real device/browser testing
- Cross-platform testing capability

### 📝 Configuration Management
- YAML-based configuration
- Multiple environment support
- Tenant-based testing

## Running Tests on BrowserStack (Optional)

### 1. Create BrowserStack Account

Visit [BrowserStack](https://www.browserstack.com) and create an account.

### 2. Update `.browserstack.yml`

```yaml
userName: YOUR_BROWSERSTACK_USERNAME
accessKey: YOUR_BROWSERSTACK_ACCESS_KEY
```

### 3. Run Tests

```bash
browserstack-sdk pytest
```

## View Test Reports

After running tests with HTML reporting:

**Windows:**
```bash
start report.html
```

**macOS:**
```bash
open report.html
```

**Linux:**
```bash
xdg-open report.html
```

## Logging and Debugging

### Enable Debug Logging

Modify `conftest.py`:
```python
logging.basicConfig(level=logging.DEBUG)
```

### Take Screenshots

Screenshots are automatically captured on test failure. Check the `screenshots/` directory.

### Use Browser Dev Tools

Set `headless: false` in `env.yaml` to keep the browser window open for inspection.

## Deactivate Virtual Environment

When done with testing:

```bash
deactivate
```

## Summary of Workflow

1. ✅ Clone the repository
2. ✅ Set up Python and create virtual environment
3. ✅ Install dependencies
4. ✅ Install Playwright browsers
5. ✅ Configure YAML files (env, credentials, tenants)
6. ✅ Run tests with pytest
7. ✅ (Optional) Run on BrowserStack for cross-device testing
8. ✅ View and analyze test reports

## Best Practices

- ✅ Always use Page Object Model pattern
- ✅ Keep selectors in the page object classes
- ✅ Use meaningful test names
- ✅ Add test markers for better organization
- ✅ Keep configuration separate from test code
- ✅ Never commit actual credentials
- ✅ Use explicit waits instead of sleep
- ✅ Take screenshots on failures
- ✅ Write descriptive assertions

## Troubleshooting

### Playwright Browsers Not Installed
```bash
python -m playwright install
```

### Port Already in Use
Change the port in `env.yaml` or kill the process using the port.

### Test Timeout Issues
Increase the `timeout` value in `env.yaml`.

### Screenshot Directory Not Found
The `screenshots/` directory is created automatically on first failure.

## Contributing

1. Create a new branch for your feature
2. Follow the existing code style
3. Add tests for new features
4. Update documentation
5. Submit a pull request

## CI/CD Integration

This framework is ready for integration with:
- GitHub Actions
- Jenkins
- GitLab CI
- Azure DevOps

Refer to `.github/workflows/` for example configurations.

## Support

For issues and support:
- 📧 Email: support@workflowpro.com
- 📖 Documentation: [WorkflowPro Docs](https://docs.workflowpro.com)
- 🐛 Report Issues: [GitHub Issues](https://github.com/yashkancharwale/workflowpro-automation/issues)

## License

This project is licensed under the MIT License - see LICENSE file for details.

---

**Happy Testing! 🚀**
