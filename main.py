import flet as ft
from flet_contrib.color_picker import ColorPicker


def main(page: ft.Page):
    page.adaptive = True  # 自适应
    page.fonts = {
        "logo": "/tittle.ttf",
        "text": "/text.ttf",
    }  # 字体
    page.theme = ft.Theme(font_family="text")
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.scroll = ft.ScrollMode.AUTO
    # 页眉/页脚
    if (
        page.platform == ft.PagePlatform.WINDOWS
        or page.platform == ft.PagePlatform.MACOS
        or page.platform == ft.PagePlatform.LINUX
    ):
        page.appbar = ft.AppBar(
            adaptive=True,
            leading=ft.Image(
                src=f"/icon.png",
                width=100,
                height=100,
                fit=ft.ImageFit.CONTAIN,
                offset=ft.transform.Offset(x=0.2, y=0),
            ),
            leading_width=35,
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
                ft.IconButton(ft.icons.BRIGHTNESS_AUTO, on_click=lambda _: dark_mode()),
                # ft.IconButton(ft.icons.FILTER_3),
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="关于", on_click=lambda _: delc(nick)),
                        ft.PopupMenuItem(text="作者のB站"),
                    ]
                ),
            ],
        )
    else:
        page.appbar = ft.AppBar(
            adaptive=True,
            leading=ft.Image(
                src=f"/icon.png",
                width=100,
                height=100,
                fit=ft.ImageFit.CONTAIN,
                offset=ft.transform.Offset(x=0.3, y=0),
            ),
            leading_width=35,
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
                ft.IconButton(ft.icons.BRIGHTNESS_AUTO, on_click=lambda _: dark_mode()),
                # ft.IconButton(ft.icons.FILTER_3),
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="关于", on_click=lambda _: delc(nick)),
                        ft.PopupMenuItem(text="作者のB站"),
                    ]
                ),
            ],
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

    # 自定义函数
    # 深色模式
    def dark_mode():
        # print(page.theme_mode)
        if page.theme_mode == ft.ThemeMode.SYSTEM:
            page.theme_mode = ft.ThemeMode.DARK
            page.appbar.actions[0].icon = ft.icons.DARK_MODE
            page.update()
        elif page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.appbar.actions[0].icon = ft.icons.WB_SUNNY_OUTLINED
            page.update()
        else:
            page.theme_mode = ft.ThemeMode.SYSTEM
            page.appbar.actions[0].icon = ft.icons.BRIGHTNESS_AUTO
            page.update()

    # 删除元素
    def delc(e):
        page.controls.remove(e)
        # e.visible = False
        page.update()

    # 颜色列表更改事件
    def color_change(e):
        tmp = ft.Row([color_picker, result])
        if colors.value == "自选颜色":
            if (
                page.platform == ft.PagePlatform.WINDOWS
                or page.platform == ft.PagePlatform.MACOS
                or page.platform == ft.PagePlatform.LINUX
            ):
                delc(result)
                copytext.expand = False
                page.add(tmp)
            else:
                delc(result)
                page.add(color_picker, result)
        else:
            if (
                page.platform == ft.PagePlatform.WINDOWS
                or page.platform == ft.PagePlatform.MACOS
                or page.platform == ft.PagePlatform.LINUX
            ):
                # print(tmp)
                # 死BUG滚啊啊啊！
                # color_picker.visible = False
                page.controls.pop()
                copytext.expand = True
                page.add(result)
            else:
                delc(color_picker)
                copytext.expand = True
                page.update()

    # 组件
    # 公用
    page.add(
        nick := ft.TextField(
            adaptive=True, label="请输入昵称", hint_text="请输入昵称..."
        ),
    )
    bold = ft.Switch(label="加粗", value=False, adaptive=True)
    itatic = ft.Switch(label="斜体", value=False, adaptive=True)
    copytext = ft.TextField(
        adaptive=True,
        label="结果",
        hint_text="复制所有内容到Phigros的名字框中...",
        multiline=True,
        min_lines=1,
        max_lines=5,
        expand=True,
    )
    # preview = ft.Row([copytext, ft.IconButton(ft.icons.COPY_OUTLINED)])
    preview = ft.Container(
        content=ft.Text(
            "Some text",
            size=30,
            text_align=ft.TextAlign.RIGHT,
            expand=True,
            color=ft.colors.WHITE,
            font_family="text",
            spans=[
                ft.TextSpan(
                    "here goes italic",
                    ft.TextStyle(italic=True, size=20, color=ft.colors.GREEN),
                    spans=[
                        ft.TextSpan(
                            "bold and italic",
                            ft.TextStyle(weight=ft.FontWeight.BOLD),
                        ),
                        ft.TextSpan(
                            "just italic",
                            spans=[
                                ft.TextSpan("smaller italic", ft.TextStyle(size=15))
                            ],
                        ),
                    ],
                )
            ],
        ),
        bgcolor=ft.colors.BLACK,
    )
    result = ft.Column(
        [
            ft.Row([copytext, ft.IconButton(ft.icons.COPY_OUTLINED)]),
            ft.Row(
                [
                    ft.Text("预览：", weight=ft.FontWeight.BOLD, size=30),
                    preview,
                ],scroll=ft.ScrollMode.HIDDEN
            ),
        ]
    )
    page.add(ft.Divider())

    # 单色
    colors = ft.Dropdown(
        label="颜色",
        hint_text="选择您喜欢的颜色...",
        on_change=color_change,
        options=[
            ft.dropdown.Option("红色"),
            ft.dropdown.Option("橙色"),
            ft.dropdown.Option("黄色"),
            ft.dropdown.Option("绿色"),
            ft.dropdown.Option("蓝色"),
            ft.dropdown.Option("靛色"),
            ft.dropdown.Option("紫色"),
            ft.dropdown.Option("自选颜色"),
        ],
    )
    color_picker = ft.Column(
        [ColorPicker(color="#c8df6f"), ft.FilledButton("设置颜色", adaptive=True)],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # CP = ft.Row([color_picker], alignment=ft.MainAxisAlignment.SPACE_AROUND, wrap=True,scroll=True)

    page.add(
        colors,
        ft.Row([bold, itatic], alignment=ft.MainAxisAlignment.SPACE_AROUND),
        ft.Divider(),
        result,
    )


ft.app(
    target=main,
    web_renderer=ft.WebRenderer.HTML,
    assets_dir="assets",
)
