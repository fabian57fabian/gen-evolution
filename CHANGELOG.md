# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Gpt llm
- Groq llm

### Changed

- Moved utils scripts to src.utils.py
- evolving summary moved to changelog
- only last summary gets written in README.md
- workflow starts only on pushing to evolve* branches

### Removed

- last_summary.txt removed
- last_summary.txt Artifact removed from llm-evolution.yml

## [0.1.0] - 2024-12-12

### Added

- Evolution script
- Cohere llm
- llm-evolution workflow on non-main branches
- PAT secret in workflow
