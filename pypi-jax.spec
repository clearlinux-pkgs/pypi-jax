#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jax
Version  : 0.3.16
Release  : 26
URL      : https://files.pythonhosted.org/packages/05/5f/7f3692fd90a6d5635683cc18f5cba6da97b9ce13874b981714593fc7a4ae/jax-0.3.16.tar.gz
Source0  : https://files.pythonhosted.org/packages/05/5f/7f3692fd90a6d5635683cc18f5cba6da97b9ce13874b981714593fc7a4ae/jax-0.3.16.tar.gz
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
Requires: pypi(etils)
Requires: pypi(numpy)
Requires: pypi(opt_einsum)
Requires: pypi(scipy)
Requires: pypi(typing_extensions)

%description python3
python3 components for the pypi-jax package.


%prep
%setup -q -n jax-0.3.16
cd %{_builddir}/jax-0.3.16
pushd ..
cp -a jax-0.3.16 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1660316495
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

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jax
cp %{_builddir}/jax-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jax/2b8b815229aa8a61e483fb4ba0588b8b6c491890
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
