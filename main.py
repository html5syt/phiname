import flet as ft

from flet_contrib.color_picker import ColorPicker


def main(page: ft.Page):
    # global nick

    # 单一事件
    # 导航栏
    def navigationTo(e: ft.ControlEvent):
        nonlocal navigation
        # 防止重复点击
        if navigation != e.data:
            navigation = e.data
            delList = [
                nick,
                divider,
                colors,
                parameter,
                divider1,
                result,
                multi_Btn,
            ]
            n = 0
            for i in delList:
                n += 1
                try:
                    page.controls.remove(i)
                    page.update()
                except:
                    print(f"error:{i},on{n}")
            if int(navigation) == 0:
                page.add(
                    nick,
                    divider,
                    colors,
                    parameter,
                    divider1,
                    result,
                )
            elif int(navigation) == 1:
                page.add(
                    # nick,
                    # divider,
                    # colors,
                    # parameter,
                    # divider1,
                    multi_Btn,
                    result,
                )
            # print(navigation)

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
                            size=15,
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
        on_change=navigationTo,
    )

    navigation = 0

    # 自定义（事件）函数
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

    # 复制文本
    def copy(e):
        page.set_clipboard(copytext.value)
        page.overlay.append(
            ft.SnackBar(
                content=ft.Text("结果已复制到剪贴板！"), open=True, duration=2000
            )
        )
        page.update()

    sizeN = None

    # 颜色处理
    def colorProssing(e: ft.ControlEvent):
        nonlocal navigation, copytext, size, colors, color_picker_ctrl, nick, sizeN
        # colors.value = colors.value
        # print("navigation:",navigation)
        # 单色部分
        # print("sizeN55556",sizeN)
        preview.content.spans[0].style = ft.TextStyle()
        if int(navigation) == 0:
            # print(e.control)
            resultTmp = nick.value
            preview.content.spans[0].text = nick.value
            # preview.content.spans[0].style=None
            if bold.value:
                resultTmp = f"<b>{resultTmp}</b>"
                # preview.content.spans[0].text=resultTmp
                preview.content.spans[0].style.weight = ft.FontWeight.BOLD
            if itatic.value:
                resultTmp = f"<i>{resultTmp}</i>"
                preview.content.spans[0].style.italic = True
            if sizeN != None:
                # print("sizeN:",sizeN)
                resultTmp = f"<size={size.value}>{resultTmp}</size>"
                preview.content.spans[0].style.size = size.value
            try:
                if "字号" == e.control.label and size.value != "0":
                    try:
                        if float(size.value) != 0:
                            size.error_text = ""
                            resultTmp = f"<size={size.value}>{resultTmp}</size>"
                            preview.content.spans[0].style.size = size.value
                            sizeN = size.value
                    except:
                        size.error_text = "请输入正确的数字！"
            except:
                if size.value != "0" or size.value != None:
                    # print("size:", type(float(size.value)))
                    try:
                        if float(size.value) != 0:
                            size.error_text = ""
                            resultTmp = f"<size={size.value}>{resultTmp}</size>"
                            preview.content.spans[0].style.size = size.value
                            sizeN = size.value
                    except:
                        size.error_text = "请输入正确的数字！"
                        sizeN = None
            for key, value in {
                "红色": "red",
                "橙色": "orange",
                "黄色": "yellow",
                "绿色": "green",
                "蓝色": "blue",
                "靛色": "#4b0082",
                "紫色": "purple",
            }.items():
                # print(colors.value)
                if colors.value == key:
                    resultTmp = f"<color={value}>{resultTmp}</color>"
                    preview.content.spans[0].style.color = value
            if colors.value == "自选颜色":
                resultTmp = f"<color={color_picker_ctrl.color}>{resultTmp}</color>"
                preview.content.spans[0].style.color = color_picker_ctrl.color
            copytext.value = f"{resultTmp}\nGearnerated by PhiName"
        if nick.value == "":
            resultTmp = ""
            copytext.value = ""
            preview.content.spans[0].text = "—暂无预览—"
        page.update()

    color = ""

    # 颜色列表更改事件
    def color_change(e):
        nonlocal color
        tmp = ft.ResponsiveRow(
            [
                ft.Column(
                    col={"xxl": 3, "xl": 4, "lg": 4, "md": 6, "sm": 6, "xs": 12},
                    controls=[color_picker],
                ),
                ft.Column(
                    col={"xxl": 9, "xl": 8, "lg": 8, "md": 6, "sm": 6, "xs": 12},
                    controls=[result],
                ),
            ],
            columns=12,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
        if colors.value == "自选颜色":
            if (
                page.platform == ft.PagePlatform.WINDOWS
                or page.platform == ft.PagePlatform.MACOS
                or page.platform == ft.PagePlatform.LINUX
            ):
                delc(result)
                copytext.expand = True
                copytext.min_lines = 1
                copytext.max_lines = 12
                copytext.width = 1000
                # tmp.scroll = ft.ScrollMode.AUTO
                page.add(tmp)
            else:
                delc(result)
                page.add(tmp)
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
                copytext.min_lines = 1
                copytext.max_lines = 11
                page.add(result)
                # fo
            else:
                page.controls.pop()
                copytext.expand = True
                page.add(result)
                # page.update()
            colorProssing(
                e,
            )

    # 组件
    # 公用区

    divider = ft.Divider()
    divider1 = ft.Divider()

    bold = ft.Switch(label="加粗 ", value=False, adaptive=True, on_change=colorProssing)
    itatic = ft.Switch(
        label="斜体", value=False, adaptive=True, on_change=colorProssing
    )

    def sizeT(e):
        nonlocal sizeN
        sizeN = None
        colorProssing(e)

    size = ft.TextField(
        adaptive=True,
        label="字号",
        expand=True,
        on_change=sizeT,
        on_submit=sizeT,
        helper_text="仅限数字，0为默认大小",
        value=0,
    )
    copytext = ft.TextField(
        adaptive=True,
        label="结果",
        helper_text="Tips: 复制所有内容到Phigros的名字框中，完成后直接退出设置界面咕~",
        multiline=True,
        min_lines=1,
        max_lines=5,
        expand=True,
    )
    # preview = ft.Row([copytext, ft.IconButton(ft.icons.COPY_OUTLINED)])
    preview = ft.Container(
        content=ft.Text(
            "",
            size=30,
            text_align=ft.TextAlign.RIGHT,
            # expand=True,
            color=ft.colors.WHITE,
            font_family="text",
            spans=[
                ft.TextSpan(text="—暂无预览—", style=ft.TextStyle()),
            ],
        ),
        bgcolor=ft.colors.BLACK,
    )
    result = ft.Column(
        [
            ft.Row([copytext, ft.IconButton(ft.icons.COPY_OUTLINED, on_click=copy)]),
            ft.Row(
                [
                    ft.Text("预览：", weight=ft.FontWeight.BOLD, size=30),
                    preview,
                ],
                scroll=ft.ScrollMode.AUTO,
            ),
        ]
    )

    # 单色/多色公用
    parameter = ft.Row(
        [bold, itatic, ft.VerticalDivider(), size],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
    )
    colors = ft.Dropdown(
        label="颜色",
        hint_text="选择您喜欢的颜色...",
        on_change=color_change,
        options=[
            ft.dropdown.Option("红色", on_click=colorProssing),
            ft.dropdown.Option("橙色", on_click=colorProssing),
            ft.dropdown.Option("黄色", on_click=colorProssing),
            ft.dropdown.Option("绿色", on_click=colorProssing),
            ft.dropdown.Option("蓝色", on_click=colorProssing),
            ft.dropdown.Option("靛色", on_click=colorProssing),
            ft.dropdown.Option("紫色", on_click=colorProssing),
            ft.dropdown.Option("自选颜色"),
        ],
        # on_click=colorProssing,
    )
    color_picker_ctrl = ColorPicker(color="#c8df6f")
    color_picker = ft.Column(
        controls=[
            color_picker_ctrl,
            ft.FilledButton(
                "设置颜色",
                adaptive=True,
                on_click=colorProssing,
                width=color_picker_ctrl.width,
            ),
        ],
        # alignment=ft.MainAxisAlignment.CENTER,
    )

    # CP = ft.Row([color_picker], alignment=ft.MainAxisAlignment.SPACE_AROUND, wrap=True,scroll=True)

    # 单色/渐变公用
    nick = ft.TextField(
        adaptive=True,
        label="请输入昵称",
        hint_text="请输入昵称...",
        on_change=colorProssing,
        on_submit=colorProssing,
    )

    #独占区
    #多色
    multi_Btn= ft.Row(
        [ft.FilledButton("开启多选",adaptive=True,expand=True),ft.FilledButton("自动填充",tooltip="Tip：长按可平均分割~",adaptive=True,expand=True)]
    )

    #初始化组件
    page.add(
        nick,
        divider,
        colors,
        parameter,
        divider1,
        result,
    )


ft.app(
    target=main,
    web_renderer=ft.WebRenderer.HTML,
    assets_dir="assets",
)
