"""Localize generated reader controls without changing story text."""

ENGLISH = {
    'lang="vi"': 'lang="en"',
    'Taloo — Thư viện truyện': 'Taloo — Story Library',
    'Chạm vào một truyện để nghe kể chuyện &amp; xem hình': 'Choose a story to read and listen',
    'Chưa có truyện.': 'No stories yet.',
    'Tự động mở truyện tiếp theo': 'Play the next story automatically',
    'Hết truyện rồi! Bé giỏi lắm!': 'The end! Well done!',
    'Bắt đầu đọc truyện': 'Read the story',
    'Đọc lại từ đầu': 'Read again',
    'Đọc lại trang này': 'Replay this page',
    'Chọn truyện khác': 'Choose another story',
    'Truyện tiếp theo': 'Next story',
    'Ẩn / hiện chữ': 'Show / hide words',
    'Phát / Dừng': 'Play / pause',
    'Trang trước': 'Previous page',
    'Trang sau': 'Next page',
    'trang truyện': 'Story page',
    'bìa truyện': 'Story cover',
    'Lời kể': 'Story words',
    'Thư viện': 'Library',
    'Đọc lại': 'Read again',
    'Tự động mở “': 'Opening “',
    '” sau ': '” in ',
    '"Bìa"': '"Cover"',
    '"Trang "': '"Page "',
}


def localize_reader(html: str, language: str) -> str:
    if language.startswith("en"):
        for original, translated in sorted(ENGLISH.items(), key=lambda item: -len(item[0])):
            html = html.replace(original, translated)
    return html
