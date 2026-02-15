%global module atomicwrites

Name:		python-atomicwrites
Version:	1.4.1
Release:	2
Summary:	Atomic wrties with race-free assertion that the target file doesn’t yet exist.
Group:		Development/Python
License:	BSD
URL:		https://github.com/untitaker/python-atomicwrites
Source0:	https://github.com/untitaker/python-atomicwrites/archive/refs/tags/%{version}/python-%{module}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

Obsoletes:	python2-%{module} < %{version}-%{release}

%description
Atomic wrties with race-free assertion that the target file doesn’t yet exist. 
This can be controlled with the overwrite parameter.
Offer imple high-level API that wraps a very flexible class-based API
with Consistent error handling across platforms.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%files
%license LICENSE
%doc CONTRIBUTING.rst README.rst
%{python_sitelib}/%{module}/
%{python_sitelib}/%{module}-%{version}-py%{pyver}.egg-info/
