# YAST2 Testing Package
# Michal Svec <msvec@suse.cz>
# $Id$
#
# norootforbuild
# neededforbuild yast2-all-packages yast2-devel-packages cracklib perl-Digest-SHA1 perl-gettext perl-OPENSSL perl-X500-DN perl-Date-Calc perl-URI dosfstools perl-Parse-RecDescent perl-Archive-Zip perl-Crypt-SmbHash perl-Compress-Zlib perl-NetxAP perl-Digest-HMAC

Name:		yast2-build-test
Version:	2.10.0
Release:	0
License:	GPL
Group:		System/YaST
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

Summary:	YaST2 Testing Package

%description
-

%prep
%setup -c -T

%build

for i in /usr/share/YaST2/clients/*.ycp; do
  ycpc -qE "$i" || failed="$failed $i"
done

if [ "$failed" != "" ]; then
  echo "  FAILED: $failed  " | tr " " "\n"
  false
fi

%install
echo 'Internal only' > README

%clean
[ "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc README
