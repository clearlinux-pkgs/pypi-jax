#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jax
Version  : 0.3.4
Release  : 9
URL      : https://files.pythonhosted.org/packages/ef/2b/4e9ddec94997ca9c9da6cbfd295258b54753bc78570762c24653522c5096/jax-0.3.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/ef/2b/4e9ddec94997ca9c9da6cbfd295258b54753bc78570762c24653522c5096/jax-0.3.4.tar.gz
Summary  : Differentiate, compile, and transform Numpy code.
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-jax-python = %{version}-%{release}
Requires: pypi-jax-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(absl_py)
BuildRequires : pypi(numpy)
BuildRequires : pypi(opt_einsum)
BuildRequires : pypi(scipy)
BuildRequires : pypi(typing_extensions)

%description
<div align="center">
<img src="https://raw.githubusercontent.com/google/jax/main/images/jax_logo_250px.png" alt="logo"></img>
</div>

%package python
Summary: python components for the pypi-jax package.
Group: Default
Requires: pypi-jax-python3 = %{version}-%{release}

%description python
python components for the pypi-jax package.


%package python3
Summary: python3 components for the pypi-jax package.
Group: Default
Requires: python3-core
Provides: pypi(jax)
Requires: pypi(absl_py)
Requires: pypi(numpy)
Requires: pypi(opt_einsum)
Requires: pypi(scipy)
Requires: pypi(typing_extensions)

%description python3
python3 components for the pypi-jax package.


%prep
%setup -q -n jax-0.3.4
cd %{_builddir}/jax-0.3.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1647712490
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
