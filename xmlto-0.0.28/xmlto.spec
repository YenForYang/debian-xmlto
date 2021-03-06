Summary: A tool for converting XML files to various formats.
Name: xmlto
Version: 0.0.28
Release: 0.1
License: GPLv2+
Group: Applications/System
#Older versions up to xmlto-0.0.20
#URL: http://cyberelk.net/tim/xmlto/
#Source0: http://cyberelk.net/tim/data/xmlto/stable/%{name}-%{version}.tar.bz2
URL: https://fedorahosted.org/xmlto/
Source0: https://fedorahosted.org/releases/x/m/%{name}/%{name}-%{version}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: docbook-xsl >= 1.56.0
BuildRequires: libxslt
BuildRequires: util-linux, flex

# We rely entirely on the DocBook XSL stylesheets!
Requires: docbook-xsl >= 1.56.0

# We need one of text-www-browsers(w3m,lynx,[e]links) for full functionality
Requires: w3m

Requires: libxslt
Requires: docbook-dtds
Requires: util-linux, flex

%description
This is a package for converting XML files to various formats using XSL
stylesheets.

%package tex
Group: Applications/System
License: GPLv2+
Summary: A set of xmlto backends with TeX requirements
# For full functionality, we need passivetex.
Requires: passivetex >= 1.11
# We require main package
Requires: xmlto = %{version}-%{release}

%description tex
This subpackage contains xmlto backend scripts which do require
PassiveTeX/TeX for functionality.

%package xhtml
Group: Applications/System
License: GPLv2+
Summary: A set of xmlto backends for xhtml1 source format
# For functionality we need stylesheets xhtml2fo-style-xsl
Requires: xhtml2fo-style-xsl
# We require main package
Requires: xmlto = %{version}-%{release}

%description xhtml
This subpackage contains xmlto backend scripts for processing
xhtml1 source format.

%prep
%setup -q

%build
%configure
make
make check

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"

[ -d %{buildroot}%{_datadir}/xmlto/xsl ] || \
  mkdir %{buildroot}%{_datadir}/xmlto/xsl

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/xmlto
%exclude %{_datadir}/xmlto/format/fo/dvi
%exclude %{_datadir}/xmlto/format/fo/ps
%exclude %{_datadir}/xmlto/format/fo/pdf
%exclude %dir %{_datadir}/xmlto/format/xhtml1/
%exclude %{_datadir}/xmlto/format/xhtml1

%files tex
%defattr(-,root,root,-)
%{_datadir}/xmlto/format/fo/dvi
%{_datadir}/xmlto/format/fo/ps
%{_datadir}/xmlto/format/fo/pdf

%files xhtml
%defattr(-,root,root,-)
%dir %{_datadir}/xmlto/format/xhtml1/
%{_datadir}/xmlto/format/xhtml1/*

%changelog
* Wed Nov 18 2015 Ondrej Vasik <ovasik@redhat.com>
- New version 0.0.28
- fix broken temp files removal
- do not detect links browser as elinks

* Tue Nov 10 2015 Ondrej Vasik <ovasik@redhat.com>
- New version 0.0.27
- remove several bashisms in scripts
- add new option --profile for preprocessing documents
  with profiling stylesheet
- fix several potential crashes in xmlif (found by static analysis)

* Sat Apr 04 2014 Ondrej Vasik <ovasik@redhat.com>
- New version 0.0.26
- fix build with automake 1.13+
- fix warning in searchpath option

* Fri Dec 02 2011 Ondrej Vasik <ovasik@redhat.com>
- New version 0.0.25
- fix the fop.extensions setting (based on fop version)
- fix handling of external data objects with fop
  (deb #568894)

* Thu Jul 14 2011 Ondrej Vasik <ovasik@redhat.com>
- New version 0.0.24
- use backend extensions by default (--noextensions
  to disable it)
- basic support for epub format
- workaround passivetex limitation for chapter titles
  starting with L (rhbz #526273)

* Mon Sep 21 2009 Ondrej Vasik <ovasik@redhat.com>
- New version 0.0.23
- added autodetection for more common tools like
  gnu cp or tail
- added option --noautosize to prevent overriding
  of user-defined or system-default paper size
- use shell built-in 'type -t' instead of 'which'
  utility for detection of file availability

* Wed Mar 25 2009 Ondrej Vasik <ovasik@redhat.com>
- New version 0.0.22
- added xhtml1 source format support
- autodetection for tools/program paths, consolidated
  error code handling
- fixed libpaper cleanup, validation check now uses
  --noent and --nonet option
- fixed broken --stringparam option

* Fri Jun 20 2008 Ondrej Vasik <ovasik@redhat.com>
- New version 0.0.21
- added dblatex experimental support
- non-mandatory libpaper support
- fixed issue of cp -a option on non-gnu systems

* Tue Jan 15 2008 Ondrej Vasik <ovasik@redhat.com>
- New version 0.0.20
- fop experimental support
- possibility to read stylesheet from STDIN, using
  recursive cp in docbook formats, preparations
  for other source formats

* Mon Nov 19 2007 Ondrej Vasik <ovasik@redhat.com>
- New version 0.0.19
- License GPLv2 , changes since last comment in NEWS

* Fri May 23 2003 Tim Waugh <twaugh@redhat.com>
- Be sure to create the xsl directory.
- README.docbook-xsl is no longer shipped.

* Wed Oct  9 2002 Tim Waugh <twaugh@redhat.com>
- Build requires docbook-xsl >= 1.56.0.

* Sun Oct  6 2002 Tim Waugh <twaugh@redhat.com>
- Remove 'BuildArch: noarch' now that we ship a compiled object.
- Run tests.
- Ship xmlif.
- Build requires docbook-xsl >= 1.52.0.

* Fri Aug 30 2002 Tim Waugh <twaugh@redhat.com>
- Bump docbook-xsl requirement to 1.52.0 for manpages.

* Fri Aug  2 2002 Tim Waugh <twaugh@redhat.com>
- The archive is now distributed in .tar.bz2 format.

* Fri Jan 25 2002 Tim Waugh <twaugh@redhat.com>
- Require the DocBook DTDs.

* Fri Jan 18 2002 Tim Waugh <twaugh@redhat.com>
- Ship README.docbook-xsl.

* Fri Nov 23 2001 Tim Waugh <twaugh@redhat.com>
- Initial spec file.
