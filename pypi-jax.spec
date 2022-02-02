#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jax
Version  : 0.2.28
Release  : 4
URL      : https://files.pythonhosted.org/packages/61/0a/9aef811fa9a5a1f0eb7e3a05a97c6ed89d0956788a83c3195088049cc882/jax-0.2.28.tar.gz
Source0  : https://files.pythonhosted.org/packages/61/0a/9aef811fa9a5a1f0eb7e3a05a97c6ed89d0956788a83c3195088049cc882/jax-0.2.28.tar.gz
Summary  : Differentiate, compile, and transform Numpy code.
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-jax-license = %{version}-%{release}
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

%package license
Summary: license components for the pypi-jax package.
Group: Default

%description license
license components for the pypi-jax package.


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
%setup -q -n jax-0.2.28
cd %{_builddir}/jax-0.2.28

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1643816714
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jax
cp %{_builddir}/jax-0.2.28/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jax/2b8b815229aa8a61e483fb4ba0588b8b6c491890
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jax/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
