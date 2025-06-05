import flet as ft
import requests # Import requests

# Placeholder function for fetching news
def fetch_news():
    # In a real application, you would fetch news from an API here.
    # For now, using placeholder data:
    return [
        {"title": "Placeholder News 1: Major Event Happens", "url": "#"},
        {"title": "Placeholder News 2: Technology Breakthrough Announced", "url": "#"},
        {"title": "Placeholder News 3: Market Trends Shift", "url": "#"}
    ]

def main(page: ft.Page):
    page.title = "Jules News"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20 # Add padding around the page

    # Logo
    logo = ft.Text("Jules News", size=50, weight=ft.FontWeight.BOLD, selectable=True) # Increased logo size

    news_items_column = ft.Column(spacing=10, alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.START)
    news_articles = fetch_news()

    if news_articles:
        for article in news_articles:
            news_items_column.controls.append(
                ft.Text(
                    spans=[
                        ft.TextSpan(
                            article["title"],
                            ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE, size=20), # Increased text size
                            url=article["url"] if article["url"] != "#" else None,
                            # For clickable links in a real app, ensure Flet version supports on_click_event for TextSpan or use a different approach like Markdown
                        )
                    ],
                )
            )
    else:
        news_items_column.controls.append(ft.Text("No news to display.", size=18))

    page.add(
        ft.Row([logo], alignment=ft.MainAxisAlignment.CENTER), # Center logo in a Row
        ft.Container(height=30), # Increased spacer after logo
        news_items_column
    )

if __name__ == "__main__":
    ft.app(target=main)
