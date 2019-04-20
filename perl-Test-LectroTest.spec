#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-LectroTest
Version  : 0.5001
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/T/TM/TMOERTEL/Test-LectroTest-0.5001.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TM/TMOERTEL/Test-LectroTest-0.5001.tar.gz
Summary  : Easy, automatic, specification-based tests.
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-LectroTest-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution Test-LectroTest,
version 0.5001:
Easy, automatic, specification-based tests

%package dev
Summary: dev components for the perl-Test-LectroTest package.
Group: Development
Provides: perl-Test-LectroTest-devel = %{version}-%{release}
Requires: perl-Test-LectroTest = %{version}-%{release}

%description dev
dev components for the perl-Test-LectroTest package.


%package license
Summary: license components for the perl-Test-LectroTest package.
Group: Default

%description license
license components for the perl-Test-LectroTest package.


%prep
%setup -q -n Test-LectroTest-0.5001

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-LectroTest
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-LectroTest/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Test/LectroTest.pm
/usr/lib/perl5/vendor_perl/5.28.2/Test/LectroTest/Compat.pm
/usr/lib/perl5/vendor_perl/5.28.2/Test/LectroTest/FailureRecorder.pm
/usr/lib/perl5/vendor_perl/5.28.2/Test/LectroTest/Generator.pm
/usr/lib/perl5/vendor_perl/5.28.2/Test/LectroTest/Property.pm
/usr/lib/perl5/vendor_perl/5.28.2/Test/LectroTest/RegressionTesting.pod
/usr/lib/perl5/vendor_perl/5.28.2/Test/LectroTest/TestRunner.pm
/usr/lib/perl5/vendor_perl/5.28.2/Test/LectroTest/Tutorial.pod

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::LectroTest.3
/usr/share/man/man3/Test::LectroTest::Compat.3
/usr/share/man/man3/Test::LectroTest::FailureRecorder.3
/usr/share/man/man3/Test::LectroTest::Generator.3
/usr/share/man/man3/Test::LectroTest::Property.3
/usr/share/man/man3/Test::LectroTest::RegressionTesting.3
/usr/share/man/man3/Test::LectroTest::TestRunner.3
/usr/share/man/man3/Test::LectroTest::Tutorial.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-LectroTest/LICENSE
