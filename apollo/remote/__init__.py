"""
Contains possible interactions with the Apollo Organisms Module
"""
import json
from apollo.client import Client


class RemoteClient(Client):
    CLIENT_BASE = '/organism/'

    def add_organism(self, common_name, organism_data, blatdb=None, genus=None,
                     species=None, public=None, non_default_translation_table=None, metadata=None):
        """
        Add an organism using the remote organism API.

        The recommended structure for the genome data tarball is as follows::

            data/
            data/names/
            data/names/root.json
            data/seq/
            data/seq/fba/
            data/seq/fba/da8/
            data/seq/fba/da8/f3/
            data/seq/fba/da8/f3/Mijalis-0.txt
            data/seq/fba/da8/f3/Mijalis-1.txt
            data/seq/fba/da8/f3/Mijalis-2.txt
            data/seq/fba/da8/f3/Mijalis-3.txt
            data/seq/fba/da8/f3/Mijalis-4.txt
            data/seq/refSeqs.json
            data/tracks/
            data/trackList.json
            data/tracks.conf

        The genome name / hashed directories below the seq folder will
        obviously be specific to your orgnaism.

        :type species: str
        :param species: Species

        :type genus: str
        :param genus: Genus

        :type blatdb: str
        :param blatdb: Server-side Blat directory for the organism

        :type public: bool
        :param public: should the organism be public

        :type common_name: str
        :param common_name: Organism common name

        :type non_default_translation_table: int
        :param non_default_translation_table: The translation table number for
                                              the organism (if different than
                                              that of the server's default)

        :type metadata: str
        :param metadata: JSON formatted arbitrary metadata

        :type organism_data: file
        :param organism_data: .tar.gz or .zip archive containing the data directory.

        :rtype: dict
        :return: a dictionary with information about the new organism
        """
        data = {
            'commonName': common_name,
        }

        if blatdb is not None:
            data['blatdb'] = blatdb
        if genus is not None:
            data['genus'] = genus
        if species is not None:
            data['species'] = species

        response = self.post('addOrganismWithSequence', list(data.items()), files={'organismData': organism_data}, autoconvert_to_json=False)
        return [x for x in response if x['commonName'] == common_name]

    def delete_organism(self, organism_id):
        """
        Remove an organism completely.

        :type organism_id: str
        :param organism_id: Organism ID Number

        :rtype: dict
        :return: a dictionary with information about the deleted organism
        """
        data = {
            'organism': organism_id,
        }

        response = self.post('deleteOrganismWithSequence', data)
        return response

    def add_track(self, organism_id, track_data, track_config):
        """
        Adds a tarball containing track data to an existing organism.

        The recommended structure for your track data tarball is as follows::

            tracks/testing2/
            tracks/testing2/Mijalis/
            tracks/testing2/Mijalis/hist-2000-0.json
            tracks/testing2/Mijalis/lf-1.json
            tracks/testing2/Mijalis/lf-2.json
            tracks/testing2/Mijalis/lf-3.json
            tracks/testing2/Mijalis/names.txt
            tracks/testing2/Mijalis/trackData.json

        And an example of the track_config supplied at the same time::

            {
                "key": "Some human-readable name",
                "label": "my-cool-track",
                "storeClass": "JBrowse/Store/SeqFeature/NCList",
                "type": "FeatureTrack",
                "urlTemplate": "tracks/testing2/{refseq}/trackData.json"
            }

        This is only the recommended structure, other directory structures /
        parameter combinations may work but were not tested by the
        python-apollo author who wrote this documentation.

        :type organism_id: str
        :param organism_id: Organism ID Number

        :type track_data: file
        :param track_data: .tar.gz or .zip archive containing the data/<track> directory.

        :type track_config: dict
        :param track_config: Track configuration

        :rtype: dict
        :return: a dictionary with information about all tracks on the organism
        """
        data = {
            'organism': organism_id,
            'trackConfig': json.dumps(track_config),
        }

        response = self.post('addTrackToOrganism', list(data.items()), files={'trackData': track_data}, autoconvert_to_json=False)
        return response

    def update_track(self, organism_id, track_config):
        """
        TODO: Broken?
        Update the configuration of a track that has already been added to the
        organism. Will not update data for the track.

        And an example of the track_config supplied::

            {
                "key": "Some human-readable name",
                "label": "my-cool-track",
                "storeClass": "JBrowse/Store/SeqFeature/NCList",
                "type": "FeatureTrack",
                "urlTemplate": "tracks/testing2/{refseq}/trackData.json"
            }

        :type organism_id: str
        :param organism_id: Organism ID Number

        :type track_config: dict
        :param track_config: Track configuration

        :rtype: dict
        :return: a dictionary with information about all tracks on the organism
        """
        data = {
            'organism': organism_id,
            'trackConfig': json.dumps(track_config),
        }

        response = self.post('updateTrackForOrganism', data)
        return response


    def delete_track(self, organism_id, track_label):
        """
        Remove a track from an organism

        :type organism_id: str
        :param organism_id: Organism ID Number

        :type track_label: str
        :param track_label: Track label

        :rtype: dict
        :return: a dictionary with information about the deleted track
        """
        data = {
            'organism': organism_id,
            'trackLabel': track_label,
        }

        response = self.post('deleteTrackFromOrganism', data)
        return response
