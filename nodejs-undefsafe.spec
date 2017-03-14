%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name undefsafe

# Tests disabled due to dependencies not in brew yet
%global enable_tests 0

Summary:       Undefined safe way of extracting object properties
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       0.0.3
Release:       5%{?dist}
License:       MIT
URL:           https://github.com/remy/undefsafe
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Source1:       https://raw.githubusercontent.com/kasicka/undefsafe/454e910123b1c24d5af2e0acc151591fc6c1d4dc/LICENSE
# https://github.com/remy/undefsafe/pull/3
BuildRequires: %{?scl_prefix}nodejs-devel
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
BuildArch:     noarch

%if 0%{?enable_tests}
BuildRequires: %{?scl_prefix}nodejs(mocha)
%endif

%description
Undefined safe way of extracting object properties

Simple function for retrieving deep object properties 
without getting "Cannot read property 'X' of undefined"

%prep
%setup -q -n package
cp -p %{SOURCE1} .

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr lib package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
mocha --ui bdd test/**/*.test.js
%endif

%files
%doc README.md LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Thu Jun 09 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.0.3-5
- Resolves: rhbz#1334856 , fixes wrong license

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.0.3-4
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.0.3-3
- Rebuilt with updated metapackage

* Wed Jan 06 2016 Tomas Hrcka <thrcka@redhat.com> - 0.0.3-2
- Enable scl macros

* Mon Dec 14 2015 Troy Dawson <tdawson@redhat.com> - 0.0.3-1
- Initial package
