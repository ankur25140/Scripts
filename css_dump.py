from pymongo import MongoClient
import unicodecsv as csv
def dbSetup() :
           client = MongoClient()
           db = client.dev
           query(db)

def query(db) :
    cursor = db['_User'].aggregate(
        [{"$lookup": {"from": 'Case', "localField": 'username', "foreignField": 'userId', "as": 'dump'}}])
    with open('names.csv', 'w') as csvfile:
        fieldnames = ['username', '_created_at', '_updated_at', 'PatientName', 'Gender', 'userId', 'casecreationDate',
                      'caseupdatedAt', 'ProblemType', 'prescription', 'Patientage', 'Lat_Long', 'Doctor', 'Stage',
                      'notes','FollowupOf','Cosmetics','AskDetails','PatientQuestion','OtherDiagnosedDetails',
                      'PeriodsDetails','Diagnosis','ProblemDuration','Location','Dandruff','CareHygiene','MedicationTaken'
                      ,'RashesSymptoms','DoctorAnswer']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        for document in cursor:
           parseAndWrite(document, writer)

def parseAndWrite(document,writer) :
     if (len(document['dump']) > 0):
         for caseData in document['dump']:
             writer.writerow({'username': document['username'], '_created_at': document['_created_at'] ,'_updated_at': document[
                 '_updated_at'] , 'PatientName': caseData.get('PatientName') ,'Gender': caseData.get('Gender') ,'userId': caseData.get(
                 'userId') ,'casecreationDate': caseData.get('creationDate') , 'caseupdatedAt' :caseData.get('updatedAt') ,'ProblemType': caseData.get(
                 'ProblemType') ,'prescription': caseData.get('prescription') ,'Patientage': caseData.get('Patientage') ,'Lat_Long': caseData.get(
                 'Lat_Long') ,'Doctor': caseData.get('Doctor') ,'Stage': caseData.get('Stage'),'notes': caseData.get('notes')
                 ,'FollowupOf': caseData.get('FollowupOf') ,'Cosmetics': caseData.get('Cosmetics') ,'AskDetails': caseData.get('AskDetails')
                 ,'PatientQuestion': caseData.get('PatientQuestion') ,'OtherDiagnosedDetails': caseData.get('OtherDiagnosedDetails') ,'PeriodsDetails': caseData.get('PeriodsDetails')
                 ,'Diagnosis': caseData.get('Diagnosis') ,'ProblemDuration': caseData.get('ProblemDuration') ,'Location': caseData.get('Location')
                 ,'Dandruff': caseData.get('Dandruff') ,'CareHygiene': caseData.get('CareHygiene') ,'MedicationTaken': caseData.get('MedicationTaken')
                 ,'RashesSymptoms': caseData.get('RashesSymptoms') ,'DoctorAnswer': caseData.get('DoctorAnswer')
})
     else:
         writer.writerow({'username': document['username'], '_created_at': document['_created_at'],'_updated_at': document['_updated_at']})

dbSetup()


