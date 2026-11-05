# Inha Cha portfolio design system

현재 구현을 기준으로 정리한 디자인 시스템. 시각적 기준은 **차분한 종이색, 선명한 타이포그래피, 여백으로 구분한 편집 디자인**이다.

실제 사용 예시는 `/design-system.html`에서 확인한다. 이 페이지는 사이트 상단 메뉴에 추가하지 않았으며, 공개 배포 시 URL로 접근할 수 있다.

## 수정 위치

- 공통 색상·폰트·글자 크기 토큰: `assets/css/site.css`의 `:root`
- 페이지별 구성: `home.css`, `projects.css`, `cv.css`
- 디자인 시스템 미리보기: `design-system.html`, `assets/css/design-system.css`
- 이전 배경 팔레트: `assets/css/saved-palettes.css`

새 요소에는 기존 CSS 변수와 컴포넌트를 우선 사용한다. 미리보기의 크기 표는 실제 구현을 설명하므로, 기준을 바꾸면 함께 갱신한다.

## Color

전체 페이지는 **Dusty Rose + Warm Paper** 배경을 공유한다. 상단에 4색 그라데이션과 그레인 질감을 쓰고, 560px 아래에서는 Warm Paper로 이어진다.

| 역할 | 토큰 | 값 |
| --- | --- | --- |
| 기본 배경 | `--color-paper` | `#F4E8E1` |
| 그라데이션 왼쪽 | `--color-lilac` | `#E8D7E4` |
| 그라데이션 중간 | `--color-rose` | `#E6D5D4` |
| 그라데이션 오른쪽 | `--color-coral` | `#DDA7A4` |
| 주요 글자 | `--color-text` | `#29272A` |
| 직책·학회·보조 본문 | `--color-text-secondary` | `#57515B` |
| 날짜·안내 | `--color-text-muted` | `#6C666C` |
| 링크·포커스 | `--color-accent` | `#643A85` |
| Home 섹션 제목 | `--color-home-heading` | `#53605E` |
| CV 섹션 제목 | `--color-cv-heading` | `#4E4852` |
| 드래그·텍스트 링크 호버 | `--highlight` | `#D8BAFF` |
| 선택 텍스트 | `--highlight-ink` | `#311947` |
| 버튼 글자 | `--color-button-text` | `#5C4B61` |
| 버튼 호버 배경 | `--color-button-hover` | `#D7BED8` |
| 버튼 호버 글자 | `--color-button-ink` | `#423447` |
| 버튼 호버 테두리 | `--color-button-hover-border` | `#A88CA9` |
| 섹션 구분선 | `--color-rule` | `rgba(92,75,97,.24)` |
| 버튼 테두리 | `--color-button-border` | `rgba(92,75,97,.38)` |

새로운 강조색을 추가하기 전에 기존 라일락·플럼 계열을 재사용한다. 배경 팔레트의 밝은 색상은 글자색으로 사용하지 않는다.

## Typography

**Instrument Sans**는 모든 페이지·섹션·논문 제목과 내비게이션·버튼에 사용한다. **Inter**는 Biography·프로젝트 본문·CV 내용·저자·날짜에 사용한다. 읽는 본문은 모두 400이다. 페이지 제목과 UI는 500, 섹션 제목과 본인 저자명은 600, 논문 제목은 400으로 구분한다.

| 토큰 | 크기 | 대표 용도 |
| --- | --- | --- |
| `--type-page` | 32px / 2rem | CV 이름, 프로젝트 제목의 최소 크기 |
| `--type-entry` | 18px / 1.125rem | Home 논문 제목, 400 / 행간 1.4 |
| `--type-body` | 17px / 1.0625rem | Biography·프로젝트 본문, 행간 1.6 |
| `--type-compact` | 16px / 1rem | CV 본문·기관명 |
| `--type-secondary` | 15px / .9375rem | 저자·직책 |
| `--type-meta` | 14px / .875rem | News·날짜·학회·안내 문구 |
| `--type-small` | 13px / .8125rem | 내비게이션·프로젝트 Role |
| `--type-caption` | 12px / .75rem | 버튼·기여도 설명 |

버튼과 기여도 설명은 12px이다. 프로젝트 페이지 제목은 `clamp(2rem, 5vw, 3.5rem)`으로 32–56px 사이에서 변한다. 일반 제목의 자간은 −.025em, 긴 본문은 −.01em, Home·CV 섹션명은 모두 Instrument Sans 14px / 600 / 행간 1.4 / 자간 .065em을 사용한다. CV 논문 제목은 같은 서체의 16px / 400이다.

## Layout and components

- 공통 프레임은 최대 1160px. 좌우 여백은 `clamp(24px, 7vw, 84px)`.
- 읽는 본문의 기본 최대 너비는 68ch. CV는 860px, 프로젝트 목록은 820px, 상세는 800px.
- 프로젝트 목록은 2열, 열 사이 16px, 행 사이 12px. 620px 이하에서는 1열.
- 프로젝트 블록 사이 32px, 나란한 이미지 사이 6px.
- CV 날짜 열은 오른쪽, 내용 열은 왼쪽 정렬. 날짜 열 136px, 간격 24px. 600px 이하에서는 104px와 16px.
- CV 섹션 제목은 본문 열 위. Research Interests는 페이지 왼쪽에 정렬한다.
- 논문은 제목 → 저자 → 짧은 학회명 → 자료 버튼 순서. 제목과 학회에는 밑줄을 넣지 않는다.
- Home 섹션 제목 아래에만 1px 선을 사용하고, 논문 사이에는 28px 여백을 둔다.
- PDF·BibTeX 버튼은 Instrument Sans 12px / 500, 최소 너비 72px, 2px 모서리, 1px 테두리.
- BibTeX 데이터가 없으면 비활성 표시. 활성 링크는 키보드 포커스와 원래 링크 동작을 유지한다.

기본 간격은 4 / 8 / 12 / 16 / 24 / 32 / 44px를 중심으로 조합한다. 반응형에서 긴 날짜는 월과 연도를 묶은 상태로 시작일과 종료일 사이에서 줄바꿈한다.
