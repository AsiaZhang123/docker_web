
import datetime
from app import db


# 秋香小程序二维码表
class QrCodeScene(db.Model):
    __tablename__ = "qrCodeScene"
    sceneID = db.Column(db.Integer, primary_key=True, autoincrement=True) # ,comment=u"主键，自增"
    scene = db.Column(db.String(512), nullable=True)
    tag = db.Column(db.Integer, nullable=True)  # , comment=u"1 职位 2 publisher店铺 3 代理商" 4 shopID店铺
    url = db.Column(db.String(512), nullable=True)
    jobID = db.Column(db.Integer, nullable=True)
    shopID = db.Column(db.Integer, nullable=True)
    publisher = db.Column(db.Integer, nullable=True)
    userID = db.Column(db.Integer, nullable=True)
    operatorID = db.Column(db.Integer, nullable=True)
    createTime = db.Column(db.DateTime, nullable=True, default=datetime.datetime.now())
    updateTime = db.Column(db.DateTime, nullable=True, default=datetime.datetime.now())

    def __init__(self,url=None,scene=None,tag=None,jobID=None,shopID=None,publisher=None,userID=None,operatorID=None,createTime=None,updateTime=None):
        self.url = url
        self.scene = scene
        self.tag = tag
        self.jobID = jobID
        self.shopID = shopID
        self.publisher = publisher
        self.userID = userID
        self.operatorID = operatorID
        self.createTime = createTime
        self.updateTime = updateTime

    def __str__(self):
        return self.sceneID

    def __repr__(self):
        return '<QRCodeScene %r>' % self.sceneID

    def save(self):
        self.updateTime = datetime.datetime.now()
        db.session.add(self)
        db.session.commit()
