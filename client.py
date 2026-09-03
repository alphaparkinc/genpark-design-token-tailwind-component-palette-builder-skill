class DesignTokenTailwindComponentPaletteBuilderClient:
    def build_design_token_palette(self, primary_brand_hex='#6366F1', surface_theme='DARK_CYBERPUNK'):
        return {
            'palette_id': 'tkn_plt_7721',
            'brand_base_color': primary_brand_hex,
            'theme_mode': surface_theme,
            'tailwind_config_tokens': {
                'colors': {
                    'brand': {'50': '#EEF2FF', '500': '#6366F1', '900': '#312E81'},
                    'background': '#090D16',
                    'foreground': '#F8FAFC',
                    'border': '#1E293B'
                },
                'borderRadius': {'card': '0.75rem', 'button': '0.5rem'}
            },
            'wcag_contrast_ratio': 11.4,
            'design_tokens_css_url': 'https://tokens.v0.genpark.ai/palettes/7721.css'
        }
