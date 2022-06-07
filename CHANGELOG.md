# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-datacatalog/#history

## [2.0.2](https://github.com/googleapis/python-datacatalog/compare/v2.0.1...v2.0.2) (2022-06-07)


### Bug Fixes

* **deps:** require protobuf<4.0.0 on v2 branch ([#394](https://github.com/googleapis/python-datacatalog/issues/394)) ([3f1fc62](https://github.com/googleapis/python-datacatalog/commit/3f1fc626e978e62ba02013ac11eb46b33a59e18f))

### [2.0.1](https://github.com/googleapis/python-datacatalog/compare/v2.0.0...v2.0.1) (2022-04-01)


### Bug Fixes

* **deps:** require google-api-core >= 1.31.5, >= 2.3.2 on v2 release ([#316](https://github.com/googleapis/python-datacatalog/issues/316)) ([3fb76a4](https://github.com/googleapis/python-datacatalog/commit/3fb76a473ee5496bd1fe4a56afef6dc651e66e2f))

## [2.0.0](https://www.github.com/googleapis/python-datacatalog/compare/v1.0.0...v2.0.0) (2020-08-20)


### ⚠ BREAKING CHANGES

* This release has breaking changes. See the [2.0.0 Migration Guide](https://github.com/googleapis/python-datacatalog/blob/master/UPGRADING.md) for details.

### Features

* Migrate API client to Microgenerator ([#54](https://www.github.com/googleapis/python-datacatalog/issues/54)) ([14fbdb8](https://www.github.com/googleapis/python-datacatalog/commit/14fbdb811688296e3978b4dfe7d4c240b5b1da5d))


### Bug Fixes

* update retry config ([#47](https://www.github.com/googleapis/python-datacatalog/issues/47)) ([1c56be7](https://www.github.com/googleapis/python-datacatalog/commit/1c56be78f1aae8dd5cd93e81188135d72cc80fdc))


### Documentation

* fix readme link ([#58](https://www.github.com/googleapis/python-datacatalog/issues/58)) ([55da34c](https://www.github.com/googleapis/python-datacatalog/commit/55da34caac42dd5959c046a50ba79375f7a41788))

## [1.0.0](https://www.github.com/googleapis/python-datacatalog/compare/v0.8.0...v1.0.0) (2020-06-17)


### Features

* release as production/stable ([#25](https://www.github.com/googleapis/python-datacatalog/issues/25)) ([6d4c3df](https://www.github.com/googleapis/python-datacatalog/commit/6d4c3df232ba933e16780231b92c830453206170)), closes [#24](https://www.github.com/googleapis/python-datacatalog/issues/24)

## [0.8.0](https://www.github.com/googleapis/python-datacatalog/compare/v0.7.0...v0.8.0) (2020-05-20)


### Features

* add `restricted_locations` to v1; add `order` to `TagField` and `TagTemplateField` in v1beta1; rename `field_path` to `tag_template_field_path` in v1beta1; add pagination support to `list_taxonomies` in v1beta1 ([#20](https://www.github.com/googleapis/python-datacatalog/issues/20)) ([7a890c2](https://www.github.com/googleapis/python-datacatalog/commit/7a890c2f87ff37f610c7246bcbf369314d87b93d))

## [0.7.0](https://www.github.com/googleapis/python-datacatalog/compare/v0.6.0...v0.7.0) (2020-04-09)


### Features

* add v1 ([#13](https://www.github.com/googleapis/python-datacatalog/issues/13)) ([21629fe](https://www.github.com/googleapis/python-datacatalog/commit/21629fed1f86bb1a2800b5213f59acc5d862e2f5))

## [0.6.0](https://www.github.com/googleapis/python-datacatalog/compare/v0.5.0...v0.6.0) (2020-02-24)


### Features

* **datacatalog:** add sample for create a fileset entry quickstart ([#9977](https://www.github.com/googleapis/python-datacatalog/issues/9977)) ([16eaf4b](https://www.github.com/googleapis/python-datacatalog/commit/16eaf4b16cdc0ce7361afb1d8dac666cea2a9db0))
* **datacatalog:** undeprecate resource name helper methods, bump copyright year to 2020, tweak docstring formatting (via synth) ([#10228](https://www.github.com/googleapis/python-datacatalog/issues/10228)) ([84e5e7c](https://www.github.com/googleapis/python-datacatalog/commit/84e5e7c340fa189ce4cffca4fdee82cc7ded9f70))
* add `list_entry_groups`, `list_entries`, `update_entry_group` methods to v1beta1 (via synth) ([#6](https://www.github.com/googleapis/python-datacatalog/issues/6)) ([b51902e](https://www.github.com/googleapis/python-datacatalog/commit/b51902e26d590f52c9412756a178265850b7d516))


### Bug Fixes

* **datacatalog:** deprecate resource name helper methods (via synth) ([#9831](https://www.github.com/googleapis/python-datacatalog/issues/9831)) ([22db3f0](https://www.github.com/googleapis/python-datacatalog/commit/22db3f0683b8aca544cd96c0063dcc8157ad7335))

## 0.5.0

11-14-2019 12:54 PST

### New Features

- add policy tag manager clients ([#9804](https://github.com/googleapis/google-cloud-python/pull/9804))

### Documentation

- add python 2 sunset banner to documentation ([#9036](https://github.com/googleapis/google-cloud-python/pull/9036))
- add sample to create a fileset entry ([#9590](https://github.com/googleapis/google-cloud-python/pull/9590))
- add sample to create an entry group ([#9584](https://github.com/googleapis/google-cloud-python/pull/9584))

### Internal / Testing Changes

- change spacing in docs templates (via synth) ([#9743](https://github.com/googleapis/google-cloud-python/pull/9743))

## 0.4.0

10-23-2019 08:54 PDT

### Implementation Changes

- remove send/recv msg size limit (via synth) ([#8949](https://github.com/googleapis/google-cloud-python/pull/8949))

### New Features

- add entry group operations ([#9520](https://github.com/googleapis/google-cloud-python/pull/9520))

### Documentation

- fix intersphinx reference to requests ([#9294](https://github.com/googleapis/google-cloud-python/pull/9294))
- remove CI for gh-pages, use googleapis.dev for api_core refs. ([#9085](https://github.com/googleapis/google-cloud-python/pull/9085))
- remove unused import from samples (via synth). ([#9110](https://github.com/googleapis/google-cloud-python/pull/9110))
- remove compatability badges from READMEs. ([#9035](https://github.com/googleapis/google-cloud-python/pull/9035))
- update intersphinx mapping for requests. ([#8805](https://github.com/googleapis/google-cloud-python/pull/8805))
- add 'search' sample (via synth). ([#8793](https://github.com/googleapis/google-cloud-python/pull/8793))

## 0.3.0

07-24-2019 15:58 PDT


### Implementation Changes
- Allow kwargs to be passed to create_channel (via synth). ([#8425](https://github.com/googleapis/google-cloud-python/pull/8425))

### New Features
- Add 'options_' argument to clients' 'get_iam_policy'; pin black version (via synth). ([#8654](https://github.com/googleapis/google-cloud-python/pull/8654))
- Add 'client_options' support, update list method docstrings (via synth). ([#8503](https://github.com/googleapis/google-cloud-python/pull/8503))

### Dependencies
- Bump minimum version for google-api-core to 1.14.0. ([#8709](https://github.com/googleapis/google-cloud-python/pull/8709))
- Update pin for 'grpc-google-iam-v1' to 0.12.3+. ([#8647](https://github.com/googleapis/google-cloud-python/pull/8647))

### Documentation
- Add get_entry sample (via synth). ([#8725](https://github.com/googleapis/google-cloud-python/pull/8725))
- Link to googleapis.dev documentation in READMEs. ([#8705](https://github.com/googleapis/google-cloud-python/pull/8705))
- Add generated samples (via synth). ([#8710](https://github.com/googleapis/google-cloud-python/pull/8710))
- Add compatibility check badges to READMEs. ([#8288](https://github.com/googleapis/google-cloud-python/pull/8288))
- Update docstrings (via synth). ([#8299](https://github.com/googleapis/google-cloud-python/pull/8299))

### Internal / Testing Changes
- Enable Sample Generator Tool for Data Catalog ([#8708](https://github.com/googleapis/google-cloud-python/pull/8708))
- Add docs job to publish to googleapis.dev. ([#8464](https://github.com/googleapis/google-cloud-python/pull/8464))

## 0.2.0

06-12-2019 12:46 PDT

### New Features

- Add search capability, tags that match a query, and IAM policies ([#8266](https://github.com/googleapis/google-cloud-python/pull/8266))
- Add protos as an artifact to library (via synth). ([#8018](https://github.com/googleapis/google-cloud-python/pull/8018))

### Documentation

- Add nox session `docs`, reorder methods (via synth). ([#7766](https://github.com/googleapis/google-cloud-python/pull/7766))
- Fix broken link to client library docs in README ([#7713](https://github.com/googleapis/google-cloud-python/pull/7713))

### Internal / Testing Changes

- Suppress checking 'cov-fail-under' in nox default session (via synth). ([#8235](https://github.com/googleapis/google-cloud-python/pull/8235))
- Fix coverage in 'types.py' (via synth). ([#8150](https://github.com/googleapis/google-cloud-python/pull/8150))
- Blacken noxfile.py, setup.py (via synth). ([#8117](https://github.com/googleapis/google-cloud-python/pull/8117))
- Add empty lines (via synth). ([#8052](https://github.com/googleapis/google-cloud-python/pull/8052))

## 0.1.0

04-15-2019 15:46 PDT

### New Features

- Initial release of Cloud Data Catalog client. ([#7708](https://github.com/googleapis/google-cloud-python/pull/7708))
