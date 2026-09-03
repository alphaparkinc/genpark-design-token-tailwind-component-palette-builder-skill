from client import DesignTokenTailwindComponentPaletteBuilderClient

def main():
    client = DesignTokenTailwindComponentPaletteBuilderClient()
    res = client.build_design_token_palette('#10B981', 'LIGHT')
    print('Tailwind Token Palette Builder: ' + res['palette_id'] + ' (Contrast: ' + str(res['wcag_contrast_ratio']) + ':1)')
    print('Theme: ' + res['theme_mode'])
    print('CSS URL: ' + res['design_tokens_css_url'])

if __name__ == '__main__':
    main()
