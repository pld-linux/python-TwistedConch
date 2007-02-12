%define 	module	TwistedConch
%define		major	0.8
%define		minor	0

Summary:	Twisted SSHv2 implementation
Summary(pl.UTF-8):   Implementacja SSHv2 dla Twisted
Name:		python-%{module}
Version:	%{major}.%{minor}
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	http://tmrc.mit.edu/mirror/twisted/Conch/%{major}/%{module}-%{version}.tar.bz2
# Source0-md5:	f3ccdd8da6b6e26b0a1eae5e54b9b0e2
URL:		http://twistedmatrix.com/projects/conch/
BuildRequires:	ZopeInterface
BuildRequires:	python-TwistedCore >= 2.5.0
BuildRequires:	python-devel >= 1:2.5
Requires:	python-TwistedCore >= 2.5.0
Requires:	python-TwistedCore-ssl >= 2.5.0
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
Summary(pl.UTF-8):   Dokumentacja do TwistedConch
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
Offline documentation for TwistedConch.

%description doc -l pl.UTF-8
Dokumentacja offline do TwistedConch.

%package examples
Summary:	Example programs for TwistedConch
Summary(pl.UTF-8):   Programy przykładowe do TwistedConch
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
%{py_sitedir}/*.egg-info
%{py_sitedir}/twisted/conch
%{py_sitedir}/twisted/plugins/*
%{_mandir}/man1/*.1*

%files doc
%defattr(644,root,root,755)
%doc doc/howto

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
