%define 	module	TwistedConch

Summary:	Twisted SSHv2 implementation
Summary(pl):	Implementacja SSHv2 dla Twisted
Name:		python-%{module}
Version:	0.5.0
Release:	0.2
License:	MIT
Group:		Libraries/Python
Source0:	http://tmrc.mit.edu/mirror/twisted/Conch/0.5/%{module}-%{version}.tar.bz2
# Source0-md5:	42961532a130bb119ae3be6b14dde28b
URL:		http://twistedmatrix.com/projects/conch/
BuildRequires:	ZopeInterface
BuildRequires:	python-devel >= 2.2
Requires:	python-Twisted >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Conch is an SSHv2 implementation using the Twisted framework. It
includes a server, client, a SFTP client, and a key generator.

%description -l pl
Conch jest implementacj± SSHv2 wykorzystuj±c± Twisted. Zawiera serwer,
klienta, klienta SFTP i generator kluczy.

%package doc
Summary:	Documentation for Twisted
Summary(pl):	Dokumentacja do Twisted
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
Offline documentation for Twisted - event-driven networking framework
written in Python.

%description doc -l pl
Dokumentacja offline do Twisted - narzêdzia do budowania rozproszonych
aplikacji sieciowych pisanych w Pythonie.

%package examples
Summary:	Example programs for Twisted
Summary(pl):	Programy przyk³adowe do Twisted
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for Twisted.

%description examples -l pl
Ten pakiet zawiera przyk³adowe programy dla Twisted.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir}/twisted,%{py_sitescriptdir},%{_mandir}/man1,%{_examplesdir}/%{name}-%{version}}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

ln -sf %{py_sitescriptdir}/twisted/conch $RPM_BUILD_ROOT%{py_sitedir}/twisted/conch

install doc/man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -ar doc/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/twisted/conch
%{py_sitescriptdir}/twisted
%{_mandir}/man1/*.1*

%files doc
%defattr(644,root,root,755)
%doc doc/howto

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
