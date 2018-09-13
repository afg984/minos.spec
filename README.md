# minos.spec
minos SPECFILE for rpmbuild

## How to use this

Download the `minos.spec` file and run:

```
rpmbuild --undefine=_disable_source_fetch -ba minos.spec
```

The `--undefine=_disable_source_fetch` is to allow rpmbuid automically download the minos source code.

## CentOS 7 dependencies

* `rpm-build` - for the `rpmbuild` command
* `gcc` - of course
* `meson` - the build system; it is in `epel-release`
* `glib2-devel` - dependency of `minos` it self
* `zeromq-devel` - dependency of `minos` itself; it is in `epel-release`

