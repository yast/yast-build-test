# YAST2 Testing Package
# Michal Svec <msvec@suse.cz>
#
# $Id$
#
# norootforbuild
# neededforbuild yast2-all-packages yast2-devel-packages cracklib dosfstools perl-Digest-SHA1 perl-gettext perl-OPENSSL perl-X500-DN perl-Date-Calc perl-URI perl-Parse-RecDescent perl-Archive-Zip perl-Crypt-SmbHash perl-Compress-Zlib perl-NetxAP perl-Digest-HMAC

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
