# YAST2 Testing Package
# Michal Svec <msvec@suse.cz>
# Stanislav Visnovsky <visnov@suse.cz>
#
# $Id$
#
# norootforbuild

Name:          yast2-build-test
Version:       2.13.2
Release:       0
License:       GPL
Group:         System/YaST
BuildRoot:     %{_tmppath}/%{name}-%{version}-build

BuildRequires:  dosfstools gcc-c++ limal-bootloader limal-ca-mgm-perl limal-devel limal-devtools perl-Archive-Zip perl-Compress-Zlib perl-Crypt-SmbHash perl-Date-Calc perl-Digest-HMAC perl-NetxAP perl-URI perl-X500-DN qt3 yast2 yast2-apparmor yast2-backup yast2-bluetooth yast2-bootloader yast2-ca-management yast2-cd-creator yast2-cim yast2-control-center yast2-core yast2-core-devel yast2-country yast2-devel yast2-devtools yast2-dhcp-server yast2-dns-server yast2-firewall yast2-firstboot yast2-hardware-detection yast2-heartbeat yast2-http-server yast2-inetd yast2-installation yast2-instserver yast2-irda yast2-iscsi-client yast2-iscsi-server yast2-kerberos-client yast2-ldap yast2-ldap-client yast2-ldap-server yast2-mail yast2-mail-aliases yast2-mail-server yast2-mouse yast2-network yast2-nfs-client yast2-nfs-server yast2-nis-client yast2-nis-server yast2-ntp-client yast2-online-update yast2-packagemanager-devel yast2-packager yast2-pam yast2-perl-bindings yast2-pkg-bindings yast2-powertweak yast2-printer yast2-profile-manager yast2-qt yast2-repair yast2-restore yast2-runlevel yast2-samba-client yast2-samba-server yast2-scanner yast2-schema yast2-security yast2-slide-show-SLES yast2-slide-show-SuSELinux yast2-slp yast2-slp-server yast2-storage yast2-storage-devel yast2-storage-evms yast2-storage-lib yast2-support yast2-sysconfig yast2-testsuite yast2-tftp-server yast2-theme-NLD yast2-theme-openSUSE yast2-trans-bg yast2-trans-bn yast2-trans-bs yast2-trans-cs yast2-trans-cy yast2-trans-da yast2-trans-de yast2-trans-el yast2-trans-en_GB yast2-trans-en_US yast2-trans-es yast2-trans-fi yast2-trans-fr yast2-trans-he yast2-trans-hu yast2-trans-it yast2-trans-ja yast2-trans-km yast2-trans-ko yast2-trans-lt yast2-trans-nb yast2-trans-nl yast2-trans-pa yast2-trans-pl yast2-trans-pt yast2-trans-pt_BR yast2-trans-ro yast2-trans-ru yast2-trans-sk yast2-trans-sl yast2-trans-sr yast2-trans-stats yast2-trans-sv yast2-trans-tr yast2-trans-uk yast2-trans-zh_CN yast2-trans-zh_TW yast2-transfer yast2-tune yast2-update yast2-users yast2-vm yast2-xml yast2-add-on
%ifnarch s390 s390x
BuildRequires:  sax2-libsax-perl yast2-boot-server yast2-phone-services yast2-sound yast2-tv yast2-x11
%endif
%ifnarch s390 s390x ppc64
BuildRequires:  yast2-power-management
%endif
Summary:        YaST2 - Testing Package

%description

%prep
%setup -c -T

%build
# Test clients
for i in /usr/share/YaST2/clients/*.ycp; do
  ycpc -qE "$i" || failed="$failed#$i"
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

