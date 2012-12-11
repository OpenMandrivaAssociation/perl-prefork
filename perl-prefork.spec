%define upstream_name    prefork
%define upstream_version 1.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Optimize module loading across forking and non-forking scenarios
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More) >= 0.47
BuildRequires:	perl(File::Spec) >= 0.82
BuildRequires:	perl(Scalar::Util) >= 1.10
BuildRequires:	perl-ExtUtils-AutoInstall >= 0.49
BuildArch:	noarch
Provides:	perl(prefork)

%description
The prefork pragma is intended to allow module writers to optimise
module loading for both scenarios with as little additional code as
possible.

The prefork.pm is intended to serve as a central and optional
marshalling point for state detection (are we running in procedural or
pre-forking mode) and to act as a relatively light-weight module loader.

Loaders and Forkers
prefork is intended to be used in two different ways.

The first is by a module that wants to indicate that another module
should be loaded before forking. This is known as a "Loader".

The other is a script or module that will be initiating the forking. It
will tell prefork.pm that it is either going to fork, or is about to
fork, and that the modules previously mentioned by the Loaders should be
loaded immediately.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/prefork.pm
%{_mandir}/*/*

%changelog
* Thu Jul 23 2009 Jérôme Quelin <jquelin@mandriva.org> 1.40.0-1mdv2010.0
+ Revision: 398938
- update to 1.04
- using %%perl_convert_version
- fixed license field

* Wed May 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.03-1mdv2010.0
+ Revision: 372655
- update to new version 1.03
- adding explicit provides since lowercase ones are not automatically extracted

* Thu Aug 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2009.0
+ Revision: 271884
- update to new version 1.02

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.01-4mdv2009.0
+ Revision: 258276
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.01-3mdv2009.0
+ Revision: 246336
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.01-1mdv2008.1
+ Revision: 136345
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 02 2007 Olivier Thauvin <nanardon@mandriva.org> 1.01-1mdv2008.0
+ Revision: 46893
- 1.01


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 1.00-2mdv2007.0
+ Revision: 108465
- rebuild
- Import perl-prefork

* Sat Sep 24 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.00-1mdk
- New version

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 0.04-1mdk
- initial Mandriva package

