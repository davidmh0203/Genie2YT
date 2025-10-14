import os
import asyncio
from pyppeteer import launch


async def convert_html_to_pdf_recursively(source_folder, destination_folder):
    """
    지정된 폴더 및 하위 폴더에 있는 모든 HTML 파일을 PDF로 변환합니다.
    """
    # 목적지 폴더가 없으면 생성
    os.makedirs(destination_folder, exist_ok=True)

    # pyppeteer로 브라우저 시작
    browser = await launch(args=['--no-sandbox'])


    # os.walk를 사용하여 모든 하위 폴더와 파일을 순회
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            # 파일이 HTML 파일인지 확인
            if file.endswith('.html') or file.endswith('.htm'):
                # 원본 HTML 파일의 전체 경로
                html_path = os.path.abspath(os.path.join(root, file))

                # PDF 파일 경로 생성
                relative_path = os.path.relpath(root, source_folder)
                output_dir = os.path.join(destination_folder, relative_path)
                os.makedirs(output_dir, exist_ok=True)

                pdf_filename = os.path.splitext(file)[0] + '.pdf'
                pdf_path = os.path.join(output_dir, pdf_filename)

                print(f'Converting {html_path} to {pdf_path}...')

                try:
                    page = await browser.newPage()
                    # 로컬 파일을 열기 위해 'file://' 스키마 사용
                    await page.goto(f'file://{html_path}', {'waitUntil': 'networkidle0'})
                    await page.pdf({'path': pdf_path, 'format': 'A4'})
                    print(f'Successfully converted {file}')

                    await page.close()
                except Exception as e:
                    print(f'Failed to convert {file}: {e}')

    await browser.close()


# --- 사용 예시 ---
if __name__ == "__main__":
    # 변환할 HTML 파일이 있는 폴더 경로
    source_folder = '/Users/iminhyeong/Downloads/Documentation/en'
    # 변환된 PDF를 저장할 폴더 경로
    destination_folder = '/Users/iminhyeong/Downloads/Documentation'

    # 비동기 함수 실행
    asyncio.get_event_loop().run_until_complete(convert_html_to_pdf_recursively(source_folder, destination_folder))
