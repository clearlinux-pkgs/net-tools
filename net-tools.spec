#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : net-tools
Version  : 2.10
Release  : 24
URL      : https://sourceforge.net/projects/net-tools/files/net-tools-2.10.tar.xz
Source0  : https://sourceforge.net/projects/net-tools/files/net-tools-2.10.tar.xz
Summary  : Basic Networking Tools
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: net-tools-bin = %{version}-%{release}
Requires: net-tools-license = %{version}-%{release}
Requires: net-tools-locales = %{version}-%{release}
Requires: net-tools-man = %{version}-%{release}
Requires: hostname
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
Requires: net-tools-license = %{version}-%{release}

%description bin
bin components for the net-tools package.


%package license
Summary: license components for the net-tools package.
Group: Default

%description license
license components for the net-tools package.


%package locales
Summary: locales components for the net-tools package.
Group: Default

%description locales
locales components for the net-tools package.


%package man
Summary: man components for the net-tools package.
Group: Default

%description man
man components for the net-tools package.


%prep
%setup -q -n net-tools-2.10
cd %{_builddir}/net-tools-2.10
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663611409
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make


%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check ||:

%install
export SOURCE_DATE_EPOCH=1663611409
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/net-tools
cp %{_builddir}/net-tools-%{version}/COPYING %{buildroot}/usr/share/package-licenses/net-tools/4cc77b90af91e615a64ae04893fdffa7939db84c
%make_install
%find_lang net-tools
## Remove excluded files
rm -f %{buildroot}*/usr/bin/hostname
rm -f %{buildroot}*/usr/share/man/man1/hostname.1
rm -f %{buildroot}*/usr/share/man/*/man1/hostname.1

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/net-tools/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
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
/usr/share/man/man1/dnsdomainname.1
/usr/share/man/man1/domainname.1
/usr/share/man/man1/nisdomainname.1
/usr/share/man/man1/ypdomainname.1
/usr/share/man/man5/ethers.5
/usr/share/man/man8/arp.8
/usr/share/man/man8/ifconfig.8
/usr/share/man/man8/nameif.8
/usr/share/man/man8/netstat.8
/usr/share/man/man8/plipconfig.8
/usr/share/man/man8/rarp.8
/usr/share/man/man8/route.8
/usr/share/man/man8/slattach.8
/usr/share/man/pt_BR/man1/dnsdomainname.1
/usr/share/man/pt_BR/man1/domainname.1
/usr/share/man/pt_BR/man1/nisdomainname.1
/usr/share/man/pt_BR/man1/ypdomainname.1
/usr/share/man/pt_BR/man8/arp.8
/usr/share/man/pt_BR/man8/ifconfig.8
/usr/share/man/pt_BR/man8/netstat.8
/usr/share/man/pt_BR/man8/rarp.8
/usr/share/man/pt_BR/man8/route.8

%files locales -f net-tools.lang
%defattr(-,root,root,-)

