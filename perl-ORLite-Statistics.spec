%define upstream_name    ORLite-Statistics
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Statistics enhancement package for ORLite
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/ORLite/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(ORLite)
BuildRequires:	perl(Statistics::Basic)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This is an enhancement module for ORLite table classes, designed to provide
easy integration with the the Statistics::Base manpage module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README LICENSE Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.30.0-2mdv2011.0
+ Revision: 655149
- rebuild for updated spec-helper

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2011.0
+ Revision: 460767
- update to 0.03

* Wed Aug 19 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 418131
- import perl-ORLite-Statistics


* Wed Aug 19 2009 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist
