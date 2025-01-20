# Migration Guide: Upgrading from PyQt5 to PyQt6

This document outlines the changes made to upgrade the project from PyQt5 to PyQt6.

## Overview

The project has been upgraded to use PyQt6 to leverage new features, improvements, and security updates.

## Changes Made

1. **Dependencies**
   - Updated `requirements.txt` to replace `PyQt5` with `PyQt6`.

2. **Import Statements**
   - Updated import statements in Python files to reflect PyQt6's module structure and naming conventions.

3. **Docker Configuration**
   - Ensured that the Docker environment installs PyQt6 instead of PyQt5.

4. **Testing**
   - Verified that the application functions correctly after the upgrade.
