from pgsync import plugin


class PlaylistsPlugin(plugin.Plugin):
    """Plugin to transform playlists documents with access control."""
    name: str = 'Playlists'

    def transform(self, doc, **kwargs) -> dict:
        """Modify the document for playlist index."""
        
        doc.setdefault('authorized_users', [])
        guests = doc.get('guests', [])
        if isinstance(guests, list):
            for guest in guests:
                if guest.get('user_id'):
                    doc['authorized_users'].append(guest.get('user_id'))
        if doc.get('user_id'):
            doc['authorized_users'].append(doc.get('user_id'))
        
        # Remove guests
        doc.pop('guests', None)

        return doc
