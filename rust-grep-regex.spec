# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate grep-regex

Name:           rust-%{crate}
Version:        0.1.5
Release:        3%{?dist}
Summary:        Use Rust's regex library with the 'grep' crate

# Upstream license specification: Unlicense/MIT
License:        Unlicense or MIT
URL:            https://crates.io/crates/grep-regex
Source:         %{crates_source}
# Initial patched metadata
# * Bump to thread_local 1, https://github.com/BurntSushi/ripgrep/commit/cb2f6ddc61b79b7acf59bb00a6be9f1740aa55b8
Patch0:         grep-regex-fix-metadata.diff
Patch1:         0001-deps-update-to-thread_local-1.0.patch

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Use Rust's regex library with the 'grep' crate.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license UNLICENSE LICENSE-MIT
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Josh Stone <jistone@redhat.com> - 0.1.5-2
- Bump to thread_local 1

* Sun Sep 08 09:27:05 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5

* Sat Aug 03 14:23:23 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 16:37:12 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.3-3
- Regenerate

* Sun Jun 09 10:14:57 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.3-2
- Regenerate

* Tue Apr 16 2019 Josh Stone <jistone@redhat.com> - 0.1.3-1
- Update to 0.1.3

* Sat Feb 16 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2

* Thu Feb 14 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-5
- Backport fix for CRLF handling

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-3
- Adapt to new packaging

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-2
- Run tests in infrastructure

* Sat Sep 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-1
- Initial package
