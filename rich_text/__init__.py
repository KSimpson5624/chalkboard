"""
RichText Package

Provides:
 - 'rt': a ready-to-use RichText instance
 - 'RichText': the base class for custom styling logic

Usage:
    from richtext import rt
    print(f'{rt.green}Success!{rt.reset}')
    print(f'{rt['green']}Success!{rt['reset]}')
"""

from .richtext import rt, RichText
__all__ = ['rt', 'RichText']