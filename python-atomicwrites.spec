%global module atomicwrites

%bcond_without python2

Name:           python-%{module}
Version:	1.4.1
Release:	2
Summary:        Atomic wrties with race-free assertion that the target file doesn’t yet exist.

Group:          Development/Python
License:        BSD
URL:            https://github.com/untitaker/python-atomicwrites
Source0:		https://github.com/untitaker/python-atomicwrites/archive/refs/tags/%{version}/python-%{module}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)

%if %{with python2}
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-setuptools
%endif

%description
Atomic wrties with race-free assertion that the target file doesn’t yet exist. 
This can be controlled with the overwrite parameter.
Offer imple high-level API that wraps a very flexible class-based API
with Consistent error handling across platforms.

%files
%license LICENSE
%doc CONTRIBUTING.rst README.rst
%{python_sitelib}/%{module}/
%{python_sitelib}/%{module}-%{version}-py%{pyver}.egg-info/

#----------------------------------------------------------------------------

%if %{with python2}
%package -n python2-%{module}
Summary:        Atomic wrties with race-free assertion that the target file doesn’t yet exist.

%description -n python2-%{module}
Atomic wrties with race-free assertion that the target file doesn’t yet exist. 
This can be controlled with the overwrite parameter.
Offer imple high-level API that wraps a very flexible class-based API
with Consistent error handling across platforms.

%files -n python2-%{module}
%license LICENSE
%doc CONTRIBUTING.rst README.rst
%{python2_sitelib}/%{module}/
%{python2_sitelib}/%{module}-%{version}-py%{py2ver}.egg-info/
%endif

#----------------------------------------------------------------------------

%prep
%setup -qn python-%{module}-%{version}

%if %{with python2}
cp -a . %py2dir
%endif

%build
%py_build

%if %{with python2}
pushd %py2dir
%py2_build
%endif

%install
%py_install

%if %{with python2}
pushd %py2dir
%py2_install
%endif

