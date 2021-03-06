#
# spec file for package yast2-build-test (Version 2.13.2)
#
# Copyright (c) 2008 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild


Name:           yast2-build-test
Version:        2.13.2
Release:        290
License:        GPL v2 or later
Group:          System/YaST
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  dosfstools gcc-c++ limal-ca-mgm-perl limal-devel limal-devtools perl-Archive-Zip perl-Compress-Zlib perl-Crypt-SmbHash perl-Date-Calc perl-Digest-HMAC perl-NetxAP perl-URI perl-X500-DN yast2-add-on yast2-add-on-creator yast2-apparmor yast2-backup yast2-bootloader yast2-ca-management yast2-control-center yast2-core-devel yast2-country yast2-devel-doc yast2-devtools yast2-dhcp-server yast2-dns-server yast2-fingerprint-reader yast2-firewall yast2-firstboot yast2-ftp-server yast2-hardware-detection yast2-heartbeat yast2-http-server yast2-inetd yast2-installation yast2-instserver yast2-irda yast2-iscsi-client yast2-iscsi-server yast2-kdump yast2-kerberos-client yast2-ldap yast2-ldap-client yast2-ldap-server yast2-live-installer yast2-mail yast2-mail-server yast2-metapackage-handler yast2-mouse yast2-ncurses yast2-network yast2-nfs-client yast2-nfs-server yast2-nis-client yast2-nis-server yast2-ntp-client yast2-online-update yast2-packagemanager-devel yast2-packager yast2-pam yast2-perl-bindings yast2-pkg-bindings yast2-printer yast2-product-creator yast2-profile-manager yast2-qt yast2-registration yast2-restore yast2-runlevel yast2-samba-client yast2-samba-server yast2-scanner yast2-schema yast2-security yast2-slide-show-SLES yast2-slide-show-SuSELinux yast2-slp yast2-slp-server yast2-storage yast2-storage-devel yast2-storage-lib yast2-support yast2-sysconfig yast2-testsuite yast2-tftp-server yast2-theme-NLD yast2-theme-openSUSE yast2-trans-bg yast2-trans-bn yast2-trans-bs yast2-trans-cs yast2-trans-cy yast2-trans-da yast2-trans-de yast2-trans-el yast2-trans-en_GB yast2-trans-en_US yast2-trans-es yast2-trans-fi yast2-trans-fr yast2-trans-he yast2-trans-hu yast2-trans-it yast2-trans-ja yast2-trans-km yast2-trans-ko yast2-trans-lt yast2-trans-nb yast2-trans-nl yast2-trans-pa yast2-trans-pl yast2-trans-pt yast2-trans-pt_BR yast2-trans-ro yast2-trans-ru yast2-trans-sk yast2-trans-sl yast2-trans-sr yast2-trans-stats yast2-trans-sv yast2-trans-tr yast2-trans-uk yast2-trans-zh_CN yast2-trans-zh_TW yast2-transfer yast2-tune yast2-update yast2-users yast2-xml
%ifnarch s390 s390x
BuildRequires:  sax2-libsax-perl yast2-boot-server yast2-phone-services yast2-sound yast2-tv yast2-x11
%endif
%ifnarch s390 s390x ppc ppc64 ia64
BuildRequires:  yast2-vm
%endif
#!BuildIgnore: tomcat5 tomcat55-common-lib
Summary:        YaST2 - Testing Package

%description
YaST2 - Testing Package

%prep
%setup -c -T

%build
# Test clients
for i in /usr/share/YaST2/clients/*.ycp; do
  ycpc -qE "$i" || failed="$failed#$i"
done
# Test command line
echo "Testing cmdline interface"
for module in `/sbin/yast -l |grep -v "Available modules"` ; do
    echo "testing yast $module..."
    /usr/lib/YaST2/bin/y2base $module '("help")' ncurses &>/dev/null &
    pid=$!
    sleep  5 && jobs -l |grep -v Done |grep $pid >/dev/null && \
    sleep 10 && jobs -l |grep -v Done |grep $pid >/dev/null && \
    sleep 20 && jobs -l |grep -v Done |grep $pid >/dev/null && \
    sleep 30 && jobs -l |grep -v Done |grep $pid >/dev/null && \
    echo "*** $module still running ***" && \
    failed="$failed#Commandline for $module" && kill $pid && sleep 1 && kill -9 $pid || true
    fg || true # let the backgrounded job fetch its kill signal
done
# Error info message
error="Build Test FAILED, look at this URL for detailed information:
http://w2d.suse.de/abuildstat/failed/$RPM_ARCH/yast2-build-test##"
# Message is confusing when building locally ...
error=""
# Show result
if [ "$failed" != "" ]; then
  echo "##FAILED:#$failed###$error" | tr "#" "\n"
  false
fi

%install
echo 'Internal only' > README

%clean
[ "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc README

%changelog
* Thu Jul 31 2008 ro@suse.de
- remove dropped packages from buildreq:
  yast2-cim, yast2-storage-evms
* Sat Mar 29 2008 coolo@suse.de
- fix build
* Mon Jan 21 2008 ro@suse.de
- use buildignore for tomcat as in yast2-schema
* Thu Dec 20 2007 ro@suse.de
- removed yast2-bluetooth from buildreq
* Wed Nov 14 2007 jsrain@suse.cz
- adapted timeouts for commandline checks to avoid void build
  failuers
* Mon Aug 13 2007 jsuchome@suse.cz
- cd-creator is product creator now
- added yast2-add-on-creator, yast2-fingerprint-reader
* Thu Aug 09 2007 jsrain@suse.cz
- in addition to current test also check presence of cmdline
  interface (#266892)
* Tue Aug 07 2007 jsrain@suse.cz
- removed yast2-power-management, added yast2-kdump and
  yast2-metapackage-handler
* Thu Jul 26 2007 jsrain@suse.cz
- yast2-devel -> yast2-devel-doc, added yast2-ftp-server
* Mon Apr 16 2007 jsrain@suse.cz
- removed yast2-powertweak
* Mon Feb 26 2007 locilka@suse.cz
- added yast2-add-on
* Wed Jan 24 2007 aosthof@suse.de
- adapt spec file so that the package yast2-vm will only be
  required by i386 and x86_64
* Wed Jan 24 2007 aosthof@suse.de
- yast2-trans-sl_SI has been renamed to yast2-trans-sl and
  yast2-theme-SuSELinux has been renamed to yast2-theme-openSUSE in
  spec file
* Wed Jan 24 2007 aosthof@suse.de
- removed yast2-bootfloppy from spec file, because this module
  doesn't exist any longer
* Mon Oct 02 2006 jsrain@suse.cz
- renamed yast2-trans-el_GR to yast2-trans-el
* Fri Apr 21 2006 visnov@suse.cz
- added yast2-online-update back
* Mon Mar 27 2006 ro@suse.de
- no yast2-x11 on s390,s390x
* Mon Mar 27 2006 ro@suse.de
- fix BuildRequires for ppc64,s390,s390x
* Fri Mar 24 2006 ro@suse.de
- removed yast2-pervasive_postgres from BuildRequires
* Fri Feb 10 2006 lrupp@suse.de
- quick Beta hack: deleted macros from BuildRequires and insert
  packages manually for build
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Wed Dec 21 2005 visnov@suse.cz
- fixed nfb for new yast2-ca-mgmt and yast2-x11
- 2.13.2
* Wed Dec 21 2005 visnov@suse.cz
- removed perl-OPENSSL from nfb
- 2.13.1
* Tue Dec 13 2005 visnov@suse.cz
- removed nfb for libsax
- 2.13.0
* Mon Jul 18 2005 jsrain@suse.cz
- fixed nfb
- 2.12.1
* Mon Jul 11 2005 jsrain@suse.cz
- adapted nfb for libsax
- 2.12.0
* Tue Jun 15 2004 msvec@suse.cz
- use yast2-all-packages abuild macro
- check everything and report final result at the end
- 2.10.0
* Wed Jun 09 2004 msvec@suse.cz
- initial version of yast2 build test
- ensure syntax correctness of all yast2 clients
- internal package
- 2.9.0
