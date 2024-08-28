import flet as ft


def main(page: ft.Page):
    page.adaptive = True  # 自适应
    page.fonts = {
        "logo": "/tittle.ttf",
        "text": "/text.ttf",
    }  # 字体
    page.theme = ft.Theme(font_family="text")
    # 页眉/页脚
    if (
        page.platform == ft.PagePlatform.WINDOWS
        or page.platform == ft.PagePlatform.MACOS
        or page.platform == ft.PagePlatform.LINUX
    ):
        page.appbar = ft.AppBar(
            leading=ft.Image(
                src=f"/icon.png",
                width=100,
                height=100,
                fit=ft.ImageFit.CONTAIN,
            ),
            leading_width=40,
            title=ft.Text(
                spans=[
                    ft.TextSpan(
                        "Phigros 彩色昵称生成器",
                        ft.TextStyle(
                            # size=20,
                            foreground=ft.Paint(
                                gradient=ft.PaintLinearGradient(
                                    begin=ft.Offset(x=0, y=0),
                                    end=ft.Offset(x=350, y=0),
                                    color_stops=[
                                        0.125,
                                        0.250,
                                        0.375,
                                        0.5,
                                        0.625,
                                        0.75,
                                        0.875,
                                    ],
                                    colors=[
                                        ft.colors.RED,
                                        ft.colors.ORANGE,
                                        ft.colors.YELLOW,
                                        ft.colors.GREEN,
                                        ft.colors.BLUE,
                                        ft.colors.INDIGO,
                                        ft.colors.PURPLE,
                                    ],
                                )
                            ),
                            shadow=ft.BoxShadow(
                                offset=ft.Offset(x=0, y=0),
                                blur_radius=20,
                                color=ft.colors.BLUE,
                            ),
                            # color=ft.colors.WHITE,
                        ),
                    ),
                ],
                text_align=ft.TextAlign.CENTER,
                font_family="logo",
            ),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
                # ft.IconButton(ft.icons.FILTER_3),
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="关于"),
                        ft.PopupMenuItem(text="作者のB站"),
                    ]
                ),
            ],
        )
    else:
        page.appbar = (
            ft.AppBar(
                # leading=ft.Icon(ft.icons.PALETTE),
                leading_width=40,
                title=ft.Text(
                    spans=[
                        ft.TextSpan(
                            "Phigros 彩色昵称生成器",
                            ft.TextStyle(
                                # size=20,
                                foreground=ft.Paint(
                                    gradient=ft.PaintLinearGradient(
                                        begin=ft.Offset(x=0, y=0),
                                        end=ft.Offset(x=350, y=0),
                                        color_stops=[
                                            0.125,
                                            0.250,
                                            0.375,
                                            0.5,
                                            0.625,
                                            0.75,
                                            0.875,
                                        ],
                                        colors=[
                                            ft.colors.RED,
                                            ft.colors.ORANGE,
                                            ft.colors.YELLOW,
                                            ft.colors.GREEN,
                                            ft.colors.BLUE,
                                            ft.colors.INDIGO,
                                            ft.colors.PURPLE,
                                        ],
                                    )
                                ),
                                shadow=ft.BoxShadow(
                                    offset=ft.Offset(x=0, y=0),
                                    blur_radius=20,
                                    color=ft.colors.BLUE,
                                ),
                                color=ft.colors.WHITE,
                            ),
                        ),
                    ],
                    text_align=ft.TextAlign.CENTER,
                    font_family="logo",
                ),
                center_title=False,
                bgcolor=ft.colors.SURFACE_VARIANT,
                actions=[
                    ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
                    # ft.IconButton(ft.icons.FILTER_3),
                    ft.PopupMenuButton(
                        items=[
                            ft.PopupMenuItem(text="关于"),
                            ft.PopupMenuItem(text="作者のB站"),
                        ]
                    ),
                ],
            ),
        )
    page.navigation_bar = ft.NavigationBar(
        adaptive=True,
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.INVERT_COLORS, label="单色"),
            ft.NavigationBarDestination(icon=ft.icons.FORMAT_COLOR_FILL, label="多色"),
            ft.NavigationBarDestination(
                icon=ft.icons.COLOR_LENS_OUTLINED,
                selected_icon=ft.icons.COLOR_LENS,
                label="渐变",
            ),
        ],
    )

    # 单色部分
    page.add(
        nick := ft.TextField(
            adaptive=True, label="请输入昵称", hint_text="请输入昵称..."
        ),
    )


ft.app(
    target=main,
    view=ft.AppView.WEB_BROWSER,
    web_renderer=ft.WebRenderer.HTML,
    assets_dir="assets",
)
