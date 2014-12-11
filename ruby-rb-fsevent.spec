#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	rb-fsevent
Summary:	Very simple & usable FSEvents API
Name:		ruby-%{pkgname}
Version:	0.9.4
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	47456c473a7e3e347c0d20ebda7bbad4
URL:		http://rubygems.org/gems/rb-fsevent
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-bundler < 2
BuildRequires:	ruby-bundler >= 1.0
BuildRequires:	ruby-guard-rspec < 5
BuildRequires:	ruby-guard-rspec >= 4.2
BuildRequires:	ruby-rspec < 3
BuildRequires:	ruby-rspec >= 2.11
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FSEvents API with Signals catching (without RubyCocoa)

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE.txt
%{ruby_vendorlibdir}/rb-fsevent.rb
%{ruby_vendorlibdir}/rb-fsevent
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
