# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2026-06-14

### Added
- Professional README with full documentation
- Shared utilities module (`utils.py`) for code deduplication
- Environment variable support via `.env` file
- Graceful exit commands ("exit", "quit", "stop", "goodbye")
- Error handling in main assistant loop
- Unit tests with pytest
- `.gitignore` for clean version control
- `requirements.txt` for dependency management
- MIT License
- Contributing guidelines
- Example scripts for Anthropic and OpenAI APIs

### Fixed
- Syntax error in time greeting (`3and` → `3 and`)
- Wrong keyboard key for YouTube pause (`space bar` → `space`)
- "Write" command replacing wrong word (`type` → `write`)
- Missing spaces in speech output for open/close commands
- Hardcoded API key moved to environment variables
- Phone number moved to environment variable

### Changed
- Reorganized AI API test scripts into `examples/` directory
- Standardized address term to "ma'am" throughout
- Improved code consistency and documentation

### Removed
- Hardcoded API keys from source code
- Auto-generated PyWhatKit log containing PII
- Unused imports in main module

### Security
- Removed hardcoded Anthropic API key
- Removed exposed phone number from log file
- Added `.env` support for all secrets
