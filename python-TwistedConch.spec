%define 	module	TwistedConch
%define		major	13.0
%define		minor	0

Summary:	Twisted SSHv2 implementation
Summary(pl.UTF-8):	Implementacja SSHv2 dla Twisted
Name:		python-%{module}
Version:	%{major}.%{minor}
Release:	2
License:	MIT
Group:		Libraries/Python
Source0:	http://twistedmatrix.com/Releases/Conch/%{major}/%{module}-%{version}.tar.bz2
# Source0-md5:	0d1c4c72302d8af6036cb897438323b7
URL:		http://twistedmatrix.com/trac/wiki/TwistedConch
BuildRequires:	ZopeInterface
BuildRequires:	python-TwistedCore >= 13.0.0
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
Requires:	python-TwistedCore >= 13.0.0
Requires:	python-TwistedCore-ssl >= 13.0.0
Obsoletes:	python-Twisted-conch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Conch is an SSHv2 implementation using the Twisted framework. It
includes a server, client, a SFTP client, and a key generator.

%description -l pl.UTF-8
Conch jest implementacją SSHv2 wykorzystującą Twisted. Zawiera serwer,
klienta, klienta SFTP i generator kluczy.

%package doc
Summary:	Documentation for TwistedConch
Summary(pl.UTF-8):	Dokumentacja do TwistedConch
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
Offline documentation for TwistedConch.

%description doc -l pl.UTF-8
Dokumentacja offline do TwistedConch.

%package examples
Summary:	Example programs for TwistedConch
Summary(pl.UTF-8):	Programy przykładowe do TwistedConch
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for TwistedConch.

%description examples -l pl.UTF-8
Ten pakiet zawiera przykładowe programy dla TwistedConch.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir}/twisted,%{py_sitescriptdir},%{_mandir}/man1,%{_examplesdir}/%{name}-%{version}}

python setup.py install \
	--install-purelib=%{py_sitedir} \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

install doc/man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -a doc/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README
%attr(755,root,root) %{_bindir}/*
%if "%{py_ver}" > "2.4"
%{py_sitedir}/*.egg-info
%endif
%{py_sitedir}/twisted/conch
%{py_sitedir}/twisted/plugins/*
%{_mandir}/man1/*.1*

%files doc
%defattr(644,root,root,755)
%doc doc/howto

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
