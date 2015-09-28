#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : net-tools
Version  : 1.60
Release  : 14
URL      : http://downloads.sourceforge.net/net-tools/net-tools-1.60.tar.bz2
Source0  : http://downloads.sourceforge.net/net-tools/net-tools-1.60.tar.bz2
Summary  : Basic Networking Tools
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: net-tools-bin
Requires: net-tools-locales
Requires: net-tools-data
Requires: net-tools-doc
BuildRequires : gettext
Patch1: build.patch
Patch2: config.patch

%description
This is a collection of the basic tools necessary for setting up networking
on a Linux machine. It includes ifconfig, route, netstat, rarp, and
various other tools.

%package bin
Summary: bin components for the net-tools package.
Group: Binaries
Requires: net-tools-data

%description bin
bin components for the net-tools package.


%package data
Summary: data components for the net-tools package.
Group: Data

%description data
data components for the net-tools package.


%package doc
Summary: doc components for the net-tools package.
Group: Documentation

%description doc
doc components for the net-tools package.


%package locales
Summary: locales components for the net-tools package.
Group: Default

%description locales
locales components for the net-tools package.


%prep
%setup -q -n net-tools-1.60
%patch1 -p1
%patch2 -p1

%build
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make check ||:

%install
rm -rf %{buildroot}
%make_install
%find_lang net-tools

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/hostname
/usr/bin/arp
/usr/bin/dnsdomainname
/usr/bin/domainname
/usr/bin/ifconfig
/usr/bin/nameif
/usr/bin/netstat
/usr/bin/nisdomainname
/usr/bin/plipconfig
/usr/bin/rarp
/usr/bin/route
/usr/bin/slattach
/usr/bin/ypdomainname

%files data
%defattr(-,root,root,-)
%exclude /usr/share/man/de_DE/man1/hostname.1
%exclude /usr/share/man/fr_FR/man1/hostname.1
%exclude /usr/share/man/pt_BR/man1/hostname.1
/usr/share/man/de_DE/man1/dnsdomainname.1
/usr/share/man/de_DE/man1/domainname.1
/usr/share/man/de_DE/man1/nisdomainname.1
/usr/share/man/de_DE/man1/ypdomainname.1
/usr/share/man/de_DE/man5/ethers.5
/usr/share/man/de_DE/man8/arp.8
/usr/share/man/de_DE/man8/ifconfig.8
/usr/share/man/de_DE/man8/netstat.8
/usr/share/man/de_DE/man8/plipconfig.8
/usr/share/man/de_DE/man8/rarp.8
/usr/share/man/de_DE/man8/route.8
/usr/share/man/de_DE/man8/slattach.8
/usr/share/man/fr_FR/man1/dnsdomainname.1
/usr/share/man/fr_FR/man1/domainname.1
/usr/share/man/fr_FR/man1/nisdomainname.1
/usr/share/man/fr_FR/man1/ypdomainname.1
/usr/share/man/fr_FR/man5/ethers.5
/usr/share/man/fr_FR/man8/arp.8
/usr/share/man/fr_FR/man8/ifconfig.8
/usr/share/man/fr_FR/man8/netstat.8
/usr/share/man/fr_FR/man8/plipconfig.8
/usr/share/man/fr_FR/man8/rarp.8
/usr/share/man/fr_FR/man8/route.8
/usr/share/man/fr_FR/man8/slattach.8
/usr/share/man/pt_BR/man1/dnsdomainname.1
/usr/share/man/pt_BR/man1/domainname.1
/usr/share/man/pt_BR/man1/nisdomainname.1
/usr/share/man/pt_BR/man1/ypdomainname.1
/usr/share/man/pt_BR/man8/arp.8
/usr/share/man/pt_BR/man8/ifconfig.8
/usr/share/man/pt_BR/man8/netstat.8
/usr/share/man/pt_BR/man8/rarp.8
/usr/share/man/pt_BR/man8/route.8

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*
%exclude /usr/share/man/man1/hostname.1

%files locales -f net-tools.lang 
%defattr(-,root,root,-)

