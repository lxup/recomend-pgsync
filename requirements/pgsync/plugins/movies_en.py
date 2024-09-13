from pgsync import plugin


class MoviesEnPlugin(plugin.Plugin):
    """Plugin to transform movies documents for English index."""
    name: str = 'MoviesEn'

    def transform(self, doc, **kwargs) -> dict:
        """Modify the document for the English movies index."""
        doc_id: str = kwargs["_id"]
        doc_index: str = kwargs["_index"]
        
        # Verify the document index
        if doc_index == 'movies_en':
            doc.setdefault('title', '')
            doc.setdefault('overview', '')
            doc.setdefault('poster_path', '')
            doc.setdefault('tagline', '')

            # Transform translations
            translations = doc.get('translations', [])
            if isinstance(translations, list):
                for translation in translations:
                    if translation.get('language_id') == 'en':
                        doc['title'] = translation.get('title', '')
                        doc['overview'] = translation.get('overview', '')
                        doc['poster_path'] = translation.get('poster_path', '')
                        doc['tagline'] = translation.get('tagline', '')
                        break
            
            # Remove translations
            doc.pop('translations', None)

        return doc
