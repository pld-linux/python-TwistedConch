%define 	module	TwistedConch
%define		major	0.7
%define		minor	0

Summary:	Twisted SSHv2 implementation
Summary(pl):	Implementacja SSHv2 dla Twisted
Name:		python-%{module}
Version:	%{major}.%{minor}
Release:	0.3
License:	MIT
Group:		Libraries/Python
Source0:	http://tmrc.mit.edu/mirror/twisted/Conch/%{major}/%{module}-%{version}.tar.bz2
# Source0-md5:	0236162d53cf7f34ed341d9179e7783b
URL:		http://twistedmatrix.com/projects/conch/
BuildRequires:	ZopeInterface
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-TwistedCore >= 2.4.0
Requires:	python-TwistedCore >= 2.4.0
Requires:	python-TwistedCore-ssl >= 2.4.0
Obsoletes:	python-Twisted-conch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Conch is an SSHv2 implementation using the Twisted framework. It
includes a server, client, a SFTP client, and a key generator.

%description -l pl
Conch jest implementacj± SSHv2 wykorzystuj±c± Twisted. Zawiera serwer,
klienta, klienta SFTP i generator kluczy.

%package doc
Summary:	Documentation for TwistedConch
Summary(pl):	Dokumentacja do TwistedConch
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
Offline documentation for TwistedConch.

%description doc -l pl
Dokumentacja offline do TwistedConch.

%package examples
Summary:	Example programs for TwistedConch
Summary(pl):	Programy przyk³adowe do TwistedConch
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for TwistedConch.

%description examples -l pl
Ten pakiet zawiera przyk³adowe programy dla TwistedConch.

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
cp -ar doc/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/twisted/conch
%{py_sitedir}/twisted/plugins/*
%{_mandir}/man1/*.1*

%files doc
%defattr(644,root,root,755)
%doc doc/howto

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
