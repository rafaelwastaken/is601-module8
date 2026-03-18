"""
Pytest configuration for FastAPI Calculator tests.
Provides shared fixtures and configuration for all tests.
"""

import pytest
import sys
from pathlib import Path

# Add the project root to the path
root_path = Path(__file__).parent.parent
sys.path.insert(0, str(root_path))


@pytest.fixture(scope="session")
def test_config():
    """Provide test configuration."""
    return {
        "base_url": "http://localhost:8000",
        "timeout": 30000,
    }


def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line(
        "markers", "unit: mark test as a unit test"
    )
    config.addinivalue_line(
        "markers", "integration: mark test as an integration test"
    )
    config.addinivalue_line(
        "markers", "e2e: mark test as an end-to-end test"
    )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
