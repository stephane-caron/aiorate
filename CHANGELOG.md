# Changelog

All notable changes to this project will be documented in this file.

## [0.9] - 2022/03/12

Bumped the version number to 0.9 as the API is stable. Starting a bug-fixing window leading to v1.0.

### Fixed

- Remove of Python 3.7 from GitHub workflow
- Remove unnecessary dependencies

## [0.3] - 2022/03/03

### Added

- Full unit test coverage
- ``Rate.remaining`` function to match the ``rospy.Rate`` API

### Changed

- Sacrify Python 3.7 support for unit testing

### Fixed

- Type annotation for ``Rate.loop`` member

## [0.2] - 2022/03/03

### Added

- Documentation
- Small example in the README
- Start CHANGELOG

### Changed

- Remove custom documentation CSS
- Update project URL

## [0.1] - 2022/02/28

### Added

- Loop rate limiter in ``Rate`` class
