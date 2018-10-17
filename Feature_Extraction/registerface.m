function [  ] = registerface( directory )
% dimention 224x224 in cnn

old_path=pwd
root_path = '../'
cd(root_path)

image_dir = directory;
landmarks_dir = strcat('Landmarks_',directory);
registered_dir=strcat('Registered_',directory)
content_image = dir(image_dir);
content_landmark = dir(landmarks_dir);

len = size(content_image,1);

for i = 3:len
    curr_image = strcat(image_dir,content_image(i).name);
    curr_landmarks = strcat(landmarks_dir,content_landmark(i).name);
    fprintf('value of a: %s   %s\n', curr_image, curr_landmarks);
    % new added
    
    %% Load sample image
    disp(sprintf('This is a demo script for the PhD toolbox. It demonstrates how to use a function from the toolbox to register a face based on manually anotated eye coordinates'));
    X=imread(curr_image);
%     figure, imshow(X,[])
    

    %Y = register_face_based_on_eyes(X,eyes,[128 100]);

    %% Reading coordinates from file

    disp('This example uses a file to read the eye coordinates from.')
    A=textread(curr_landmarks);
    eyes.x(1)=A(1);  
    eyes.y(1)=A(2); 
    eyes.x(2)=A(3);
    eyes.y(2)=A(4);
    disp('Extracting grey-scale face region of size 128x128 pixels.')
    %Y = mean(register_face_based_on_eyes(X,eyes,[128 128]),3);
    Y = register_face_based_on_eyes(X,eyes,[224 224]);
%     figure
%     imshow(Y,[]);
    save_path = strcat(registered_dir,content_image(i).name)
    imwrite(Y,save_path);
end
cd(old_path)
end

