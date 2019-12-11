%global tarName atomicwrites

Name:           python-%{tarName}
Version:        1.3.0
Release:        2
Summary:        Atomic wrties with race-free assertion that the target file doesn’t yet exist.

Group:          Development/Python
License:        BSD
URL:            https://github.com/untitaker/python-atomicwrites
Source0:        https://github.com/untitaker/python-atomicwrites/archive/python-%{tarName}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:	python-setuptools
BuildRequires:	python2-devel
BuildRequires:	python2-setuptools

%description
Atomic wrties with race-free assertion that the target file doesn’t yet exist. 
This can be controlled with the overwrite parameter.
Offer imple high-level API that wraps a very flexible class-based API
with Consistent error handling across platforms.

%package -n python2-%{tarName}

Summary:        Atomic wrties with race-free assertion that the target file doesn’t yet exist.
%description -n python2-%{tarName}
Atomic wrties with race-free assertion that the target file doesn’t yet exist. 
This can be controlled with the overwrite parameter.
Offer imple high-level API that wraps a very flexible class-based API
with Consistent error handling across platforms.

%prep
%setup -qn python-%{tarName}-%{version}

cp -a . %py2dir
%build
python setup.py build

pushd %py2dir
python2 setup.py build

%install
python setup.py install --root=%{buildroot}

pushd %py2dir
python2 setup.py install --root=%{buildroot}

%files
%{py_puresitedir}/*/*
%doc CONTRIBUTING.rst README.rst LICENSE

%files -n python2-%{tarName}
%{py2_puresitedir}/*/*
%doc CONTRIBUTING.rst README.rst LICENSE
