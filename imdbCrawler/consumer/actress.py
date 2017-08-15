class ActressConsumer:
    actress_id = None
    actress_link = None
    actress_name = None
    actress_photo = {}

    def __init__(self, data=dict()):
        if data:
            self.set_dict(data)
        else:
            self.reset_dict()

    def get_dict(self, prefix='actress_'):
        response = dict()
        response.update({'{}id'.format(prefix) : self.actress_id})
        response.update({'{}link'.format(prefix) : self.actress_link})
        response.update({'{}name'.format(prefix) : self.actress_name})
        response.update({'{}photo'.format(prefix) : self.actress_photo})

        return response

    def set_dict(self, data):
        self.actress_id = str(data.get('actress_id').encode('utf-8')) if data.get('actress_id') is not None else None
        self.actress_link = str(data.get('actress_link').encode('utf-8')) if data.get('actress_link') is not None else None
        self.actress_name = str(data.get('actress_name').encode('utf-8')) if data.get('actress_name') is not None else None
        self.actress_photo = data.get('actress_photo') if data.get('actress_photo') is not None else {}

    def reset_dict(self):
        self.actress_id = None
        self.actress_link = None
        self.actress_name = None
        self.actress_photo = None



if __name__ == '__main__':
    a = ActressConsumer()
    print a.get_dict()